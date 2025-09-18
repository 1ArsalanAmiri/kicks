from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView, ProductCategoryView, ProductFilterView,
)

urlpatterns = [
    # Products
    path("", ProductListCreateView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="product-detail"),
    path("categories/", ProductCategoryView.as_view(), name="product-list-create"),
    path("filter/", ProductFilterView.as_view(), name="product-filter"),

]