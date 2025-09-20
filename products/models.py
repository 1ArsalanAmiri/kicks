from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify



class ProductSize(models.Model):
    value = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.value



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



class Product(models.Model):

    title = models.CharField(max_length=255)
    description_text = models.TextField()
    description_options = models.JSONField(default=list, blank=True)
    slug = models.SlugField(unique=True , blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.JSONField(default=list, blank=True)
    genders = models.JSONField(default=list, blank=True)  # ["Men", "Women" , "Kids"]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.ManyToManyField(ProductSize, blank=True)
    colors = models.JSONField(default=list, blank=True)
    is_new_release = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    review = models.DecimalField(max_digits=2, decimal_places=1,validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)

    @property
    def similar_products_ids(self):
        return list(Product.objects.filter(categories__in=self.categories.all()).exclude(id=self.id).distinct().values_list('id', flat=True))


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    filename = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
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