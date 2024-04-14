from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, {email}, {message}')
        return render(request, 'catalog/contacts.html')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    login_url = reverse_lazy('users:login')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        products = Product.objects.all()
        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active=True)
            if active_versions:
                product.active_versions = active_versions.last().version_name
            else:
                product.active_versions = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    login_url = reverse_lazy('users:login')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    login_url = reverse_lazy('users:login')
    permission_required = 'catalog.add_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        context_data = self.get_context_data().get('formset')

        if context_data.is_valid():
            context_data.instance = self.object
            context_data.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'
    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.is_staff:
            return ProductModeratorForm
        else:
            return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def test_func(self):
        user = self.request.user
        instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog.set_published',
            'catalog.set_description',
            'catalog.set_category',
        )

        if user == instance.owner:
            return True
        elif user.groups.filter(name='moderators') and user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object
