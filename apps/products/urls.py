"""urls"""
from django.urls import path
from .views import *

urlpatterns = [
    path('products', ProductListView.as_view(), name='product-list'),
    path('products/<product_slug>',
         ProductDetailView.as_view(), name='product-detail'),


    path('categories', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>', CategoryDetailView.as_view(),
         name='category-detail'),
    path('categories/<int:category_id>/products',
         CategoryProductListView.as_view(), name='category-product-list'),

    path('products/search/<search_term>',
         SearchProductView.as_view(), name='search-product'),
]
