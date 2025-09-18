from rest_framework import serializers
from .models import *


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['value' , "active"]


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['name' , "code"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['filename']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description_text' , 'categories' , 'review' , 'tags']


class ProductDetailSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True)
    similar_products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description_text', 'description_options',
            'categories', 'genders', 'price', 'sizes', 'colors',
            'is_new_release', 'review', 'similar_products', 'images',
            'is_available', 'stock', 'tags'
        ]

    def create(self, validated_data):
        sizes_data = validated_data.pop('sizes', [])
        colors_data = validated_data.pop('colors', [])
        similar_products_data = validated_data.pop('similar_products', [])
        tags_data = validated_data.pop('tags', [])

        product = Product.objects.create(**validated_data)

        for size in sizes_data:
            size_obj, _ = ProductSize.objects.get_or_create(**size)
            product.sizes.add(size_obj)

        for color in colors_data:
            color_obj, _ = ProductColor.objects.get_or_create(**color)
            product.colors.add(color_obj)

        for tag in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(**tag)
            product.tags.add(tag_obj)

        for similar in similar_products_data:
            if similar.id != product.id:
                product.similar_products.add(similar)

        return product

    def update(self, instance, validated_data):
        sizes_data = validated_data.pop('sizes', None)
        colors_data = validated_data.pop('colors', None)
        similar_products_data = validated_data.pop('similar_products', None)
        tags_data = validated_data.pop('tags', None)


        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if sizes_data is not None:
            instance.sizes.clear()
            for size in sizes_data:
                size_obj, _ = ProductSize.objects.get_or_create(**size)
                instance.sizes.add(size_obj)

        if colors_data is not None:
            instance.colors.clear()
            for color in colors_data:
                color_obj, _ = ProductColor.objects.get_or_create(**color)
                instance.colors.add(color_obj)

        if similar_products_data is not None:
            instance.similar_products.clear()
            for similar in similar_products_data:
                if similar.id != instance.id:
                    instance.similar_products.add(similar)

        if tags_data is not None:
            instance.tags.clear()
            for tag in tags_data:
                tag_obj, _ = Tag.objects.get_or_create(**tag)
                instance.tags.add(tag_obj)


        return instance


class ProductSerializer(serializers.ModelSerializer):
    sizes = ProductSizeSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    categories = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Category.objects.all()
    )
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )
    similar_products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), required=False
    )
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id", "title", "slug", "description_text", "description_options",
            "categories", "genders", "price", "discount", "discounted_price",
            "is_new_release", "review", "similar_products", "tags",
            "sizes", "colors", "images"
        ]

    def get_discounted_price(self, obj):
        return obj.get_discounted_price()