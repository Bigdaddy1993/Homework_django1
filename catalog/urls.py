from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='home'),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_from_pk'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]
