from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body', 'is_published', 'image')
    success_url = reverse_lazy('materials:create')

    def form_valid(self, form):
        if form.is_valid():
            new_materials = form.save()
            new_materials.slug = slugify(new_materials.title)
            new_materials.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание материала'
        return context


class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'материалы'
        return context


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body', 'is_published', 'image')

    def form_valid(self, form):
        if form.is_valid():
            new_materials = form.save()
            new_materials.slug = slugify(new_materials.title)
            new_materials.save()
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')
