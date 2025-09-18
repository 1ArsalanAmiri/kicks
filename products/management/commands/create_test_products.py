from django.core.management.base import BaseCommand
from products.models import *


TEST_PRODUCTS = [
  {
    "title": "Super Sneakers 1",
    "description_text": "Comfortable running shoes",
    "description_options": ["Lightweight", "Breathable"],
    "categories": ["Running", "Gym"],
    "genders": ["Men"],
    "price": "120.50",
    "sizes": [{"value": "42", "active": True}, {"value": "43", "active": True}],
    "colors": [{"name": "Red", "code": ""}, {"name": "Blue", "code": ""}],
    "is_new_release": True,
    "review": "4.5",
    "tags": ["Sport", "Sale"]
  },
  {
    "title": "Super Sneakers 2",
    "description_text": "Lightweight gym shoes",
    "description_options": ["Flexible", "Stylish"],
    "categories": ["Gym"],
    "genders": ["Women"],
    "price": "110.00",
    "sizes": [{"value": "38", "active": True}, {"value": "39", "active": True}],
    "colors": [{"name": "White", "code": ""}],
    "is_new_release": False,
    "review": "4.0",
    "tags": ["Fitness"]
  },
  {
    "title": "Super Sneakers 3",
    "description_text": "Casual sneakers",
    "description_options": ["Durable", "Lightweight"],
    "categories": ["Casual"],
    "genders": ["Men", "Women"],
    "price": "95.00",
    "sizes": [{"value": "40", "active": True}],
    "colors": [{"name": "Black", "code": ""}],
    "is_new_release": True,
    "review": "4.8",
    "tags": ["Casual"]
  },
  {
    "title": "Super Sneakers 4",
    "description_text": "Stylish trainers",
    "description_options": ["Fashionable", "Lightweight"],
    "categories": ["Gym", "Casual"],
    "genders": ["Women"],
    "price": "130.00",
    "sizes": [{"value": "37", "active": True}, {"value": "38", "active": True}],
    "colors": [{"name": "Pink", "code": ""}],
    "is_new_release": False,
    "review": "3.9",
    "tags": ["Fashion"]
  },
  {
    "title": "Super Sneakers 5",
    "description_text": "Running shoes for long distance",
    "description_options": ["Comfortable", "Supportive"],
    "categories": ["Running"],
    "genders": ["Men"],
    "price": "140.00",
    "sizes": [{"value": "42", "active": True}, {"value": "44", "active": True}],
    "colors": [{"name": "Blue", "code": ""}],
    "is_new_release": True,
    "review": "4.7",
    "tags": ["Sport"]
  },
  {
    "title": "Super Sneakers 6",
    "description_text": "Everyday casual shoes",
    "description_options": ["Lightweight", "Soft"],
    "categories": ["Casual"],
    "genders": ["Women"],
    "price": "90.00",
    "sizes": [{"value": "38", "active": True}, {"value": "39", "active": True}],
    "colors": [{"name": "White", "code": ""}],
    "is_new_release": False,
    "review": "4.2",
    "tags": ["Daily"]
  },
  {
    "title": "Super Sneakers 7",
    "description_text": "High-performance running shoes",
    "description_options": ["Breathable", "Lightweight"],
    "categories": ["Running"],
    "genders": ["Men"],
    "price": "150.00",
    "sizes": [{"value": "43", "active": True}, {"value": "44", "active": True}],
    "colors": [{"name": "Red", "code": ""}],
    "is_new_release": True,
    "review": "4.9",
    "tags": ["Sport", "Performance"]
  },
  {
    "title": "Super Sneakers 8",
    "description_text": "Trendy street sneakers",
    "description_options": ["Stylish", "Lightweight"],
    "categories": ["Casual", "Streetwear"],
    "genders": ["Men", "Women"],
    "price": "115.00",
    "sizes": [{"value": "40", "active": True}, {"value": "41", "active": True}],
    "colors": [{"name": "Black", "code": ""}],
    "is_new_release": False,
    "review": "4.1",
    "tags": ["Fashion"]
  },
  {
    "title": "Super Sneakers 9",
    "description_text": "Gym trainers",
    "description_options": ["Supportive", "Durable"],
    "categories": ["Gym"],
    "genders": ["Women"],
    "price": "125.00",
    "sizes": [{"value": "37", "active": True}, {"value": "38", "active": True}],
    "colors": [{"name": "Pink", "code": ""}],
    "is_new_release": True,
    "review": "4.6",
    "tags": ["Fitness"]
  },
  {
    "title": "Super Sneakers 10",
    "description_text": "All-purpose sneakers",
    "description_options": ["Comfortable", "Versatile"],
    "categories": ["Running", "Casual"],
    "genders": ["Men", "Women"],
    "price": "135.00",
    "sizes": [{"value": "42", "active": True}, {"value": "43", "active": True}],
    "colors": [{"name": "Blue", "code": ""}],
    "is_new_release": False,
    "review": "4.3",
    "tags": ["Sport", "Casual"]
  }
]

class Command(BaseCommand):
    help = 'Create n test products'

    def handle(self, *args, **kwargs):
        for prod_data in TEST_PRODUCTS:
            # Categories
            category_objs = []
            for cat_name in prod_data.get("categories", []):
                cat_obj, _ = Category.objects.get_or_create(name=cat_name)
                category_objs.append(cat_obj)

            # Tags
            tag_objs = []
            for tag_name in prod_data.get("tags", []):
                tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                tag_objs.append(tag_obj)

            # Sizes
            size_objs = []
            for size_val in prod_data.get("sizes", []):
                size_obj, _ = ProductSize.objects.get_or_create(value=size_val)
                size_objs.append(size_obj)

            # Colors
            color_objs = []
            for color_name in prod_data.get("colors", []):
                color_obj, _ = ProductColor.objects.get_or_create(name=color_name)
                color_objs.append(color_obj)

            # Product
            product, created = Product.objects.get_or_create(
                title=prod_data["title"],
                defaults={
                    "description_text": prod_data["description_text"],
                    "description_options": prod_data["description_options"],
                    "genders": prod_data["genders"],
                    "price": prod_data["price"],
                    "is_new_release": prod_data["is_new_release"],
                    "review": prod_data["review"],
                }
            )


            product.categories.set(category_objs)
            product.tags.set(tag_objs)
            product.sizes.set(size_objs)
            product.colors.set(color_objs)

            product.save()
            self.stdout.write(self.style.SUCCESS(f'Product created: {product.title}'))
