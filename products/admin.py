from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_available", "stock")
    list_filter = ("is_new_release", "categories", "genders", "tags")
    search_fields = ("title", "description_text")
    ordering = ("-id",)

    inlines = [ProductImageInline]

    filter_horizontal = ("sizes", "colors", "similar_products", "categories", "tags")



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
