from django.contrib import admin
from .models import Product, ProductImage, ProductSize, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('filename', 'alt_text', 'order', 'image_type')
    readonly_fields = ()
    ordering = ('order',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'is_available', 'stock', 'is_new_release', 'review')
    readonly_fields = ('slug','categories')
    list_filter = ('is_available', 'is_new_release', 'categories', 'genders')
    search_fields = ('title', 'slug', 'tags')
    inlines = [ProductImageInline]
    filter_horizontal = ('categories', 'sizes')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('value', 'active')
    list_filter = ('active',)
    search_fields = ('value',)
