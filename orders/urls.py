from django.urls import path
from .views import CartView, CartItemAddView, OrderListView

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart-detail"),
    path("cart/add/", CartItemAddView.as_view(), name="cart-add-item"),
    path("", OrderListView.as_view(), name="order-list"),
]
