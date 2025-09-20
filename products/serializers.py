from rest_framework import serializers
from .models import *


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['value' , "active"]



class ProductMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price", "review"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["filename"]
        # fields = []


class ProductListSerializer(serializers.ModelSerializer):
    # tags = serializers.ListField(child=serializers.CharField(max_length=7),required=False)
    categories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')
    class Meta:
        model = Product
        fields = ['id', 'title','slug', 'price', 'description_text' , 'categories' , 'review' , 'tags']


class ProductDetailSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = serializers.ListField(child=serializers.CharField(max_length=7),required=False)
    images = ProductImageSerializer(many=True, read_only=True)
    tags = serializers.ListField(child=serializers.CharField(max_length=20),required=False)
    categories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')


    class Meta:
        model = Product
        fields = [
            'id', 'title','slug', 'description_text', 'description_options',
            'categories', 'genders', 'price', 'sizes', 'colors',
            'is_new_release', 'review', 'images',
            'is_available', 'stock', 'tags'
        ]

    def create(self, validated_data):
        sizes_data = validated_data.pop("sizes", [])
        product = Product.objects.create(**validated_data)

        for size in sizes_data:
            size_obj, _ = ProductSize.objects.get_or_create(**size)
            product.sizes.add(size_obj)

        return product


    def update(self, instance, validated_data):
        sizes_data = validated_data.pop("sizes", None)

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
    categories = serializers.SlugRelatedField(many=True,read_only=True,slug_field='name')

    class Meta:
        model = Product
        fields = [
            "id", "title", "description_text", "description_options","slug",
            "categories", "genders", "price",
            "is_new_release", "review", "similar_products", "tags",
            "sizes", "colors", "images"
        ]


class ProductSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["slug"]