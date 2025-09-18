from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class ProductSize(models.Model):
    value = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.value} ({'active' if self.active else 'inactive'})"



class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.code})" if self.code else self.name



class Product(models.Model):


    title = models.CharField(max_length=255)
    description_text = models.TextField()
    description_options = models.JSONField(default=list, blank=True)
    categories = models.ManyToManyField(Category, related_name="products", blank=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    genders = models.JSONField(default=list, blank=True)  # ["Men", "Women"]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.ManyToManyField(ProductSize, blank=True)
    colors = models.ManyToManyField(ProductColor, blank=True)
    is_new_release = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    review = models.DecimalField(
        max_digits=3, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    similar_products = models.ManyToManyField('self', blank=True)


    def __str__(self):
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    filename = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)  # ترتیب نمایش
    image_type = models.CharField(
        max_length=20,
        choices=[
            ("thumbnail", "Thumbnail"),
            ("gallery", "Gallery"),
            ("banner", "Banner"),
        ],
        default="gallery"
    )

    def __str__(self):
        return f"{self.product.title} - {self.filename}"