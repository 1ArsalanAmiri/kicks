from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from .filters import ProductFilter
from .serializers import *
from .pagination import ProductPagination


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
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
    permission_classes = [IsAdminOrReadOnly]
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


class ProductCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        categories = set()
        for product in Product.objects.all():
            categories.update(product.categories or [])

        return Response({"categories": list(categories)})



class ProductFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()

        sizes = self.request.query_params.getlist('size')
        colors = self.request.query_params.getlist('color')
        categories = self.request.query_params.getlist('category')
        genders = self.request.query_params.getlist('gender')
        sort = self.request.query_params.get('sort', 'id')

        if sizes:
            qs = qs.filter(sizes__value__in=sizes)
        if colors:
            qs = qs.filter(colors__name__in=colors)
        if categories:
            qs = qs.filter(categories__contains=categories)
        if genders:
            qs = qs.filter(genders__contains=genders)

        qs = qs.order_by(sort).distinct()
        return qs
