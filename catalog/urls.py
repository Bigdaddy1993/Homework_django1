from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product_from_pk

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('<int:pk>/', product_from_pk, name='product_from_pk'),

]
