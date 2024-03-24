from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_from_pk'),

]
