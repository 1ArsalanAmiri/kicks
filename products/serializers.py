from rest_framework import serializers
from .models import *


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['value' , "active"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["filename"]
        # fields = []


class ProductListSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=7),required=False)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description_text' , 'categories' , 'review' , 'tags']


class ProductDetailSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = serializers.ListField(child=serializers.CharField(max_length=7),required=False)
    images = ProductImageSerializer(many=True, read_only=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=20),required=False)
    similar_products = serializers.SerializerMethodField()
    categories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description_text', 'description_options',
            'categories', 'genders', 'price', 'sizes', 'colors',
            'is_new_release', 'review', 'similar_products', 'images',
            'is_available', 'stock', 'tags'
        ]

    def get_similar_products(self, obj):
        return obj.similar_products_ids

    def create(self, validated_data):
        sizes_data = validated_data.pop('sizes', [])
        colors_data = validated_data.pop('colors', [])
        tags_data = validated_data.pop('tags', [])
        product = Product.objects.create(**validated_data)

        for size in sizes_data:
            size_obj, _ = ProductSize.objects.get_or_create(**size)
            product.sizes.add(size_obj)
        return product

    def update(self, instance, validated_data):
        sizes_data = validated_data.pop('sizes', None)
        colors_data = validated_data.pop('colors', None)
        tags_data = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if sizes_data is not None:
            instance.sizes.clear()
            for size in sizes_data:
                size_obj, _ = ProductSize.objects.get_or_create(**size)
                instance.sizes.add(size_obj)
        return instance


class ProductSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = serializers.ListField(child=serializers.CharField(max_length=7),required=False)
    images = ProductImageSerializer(many=True, read_only=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=20),required=False)
    similar_products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all(), required=False)

    class Meta:
        model = Product
        fields = [
            "id", "title", "description_text", "description_options",
            "categories", "genders", "price",
            "is_new_release", "review", "similar_products", "tags",
            "sizes", "colors", "images"
        ]
