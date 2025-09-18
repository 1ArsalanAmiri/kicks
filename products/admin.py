# products/admin.py
from django.contrib import admin
from .models import Product, ProductSize, ProductImage, Tag, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_new_release', 'is_available', 'stock', 'display_categories')
    list_filter = ('is_new_release', 'is_available', 'categories', 'tags')
    search_fields = ('title', 'description_text')
    ordering = ('-id',)

    def display_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    display_categories.short_description = 'Categories'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'filename')
    search_fields = ('product__title', 'filename')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('value', 'active')
    list_filter = ('active',)