from rest_framework import generics, filters
from .serializers import *
from .pagination import ProductPagination
from .serializers import ProductDetailSerializer
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description_text', 'categories', 'genders']
    ordering_fields = ['price', 'review', 'id']
    ordering = ['-id']


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductDetailSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
            context = super().get_serializer_context()
            product = self.get_object()
            similar_products = Product.objects.filter(categories__overlap=product.categories).exclude(product.id)
            context['similar_products'] = similar_products
            return context
