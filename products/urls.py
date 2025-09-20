# products/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path("" , ProductListCreateView.as_view(), name= "product-list"),
    path("<slug:slug>" , ProductDetailView.as_view(), name= "product-detail"),
    path("slugs/", ProductSlugsView.as_view(), name="product-slugs"),
    path("filter/", ProductFilterView.as_view(), name="product-filter"),
    path("<slug:slug>/similar/", SimilarProductsView.as_view(), name="similar-products"),

]
