from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    image = models.ImageField()
    url = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    STATUSES = (
        ('a', 'Active'),
        ('d', 'Deactive'),
    )
    status = models.CharField(max_length=2, choices=STATUSES)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(BaseModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Shop(BaseModel):
    address = models.TextField(max_length=1000)
    email = models.EmailField(blank=True, max_length=48, verbose_name='E Mail')
    shop_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    commission = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Affiliate(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', null=True)


class Product(BaseModel):
    related_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Receipt(BaseModel):
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)
