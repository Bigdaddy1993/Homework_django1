from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, {email}, {message}')
    return render(request, 'catalog/contacts.html')


def home(request):
    content = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', content)


def product_from_pk(request, pk):
    content = {
        'object_list': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/product_from_pk.html', content)
