from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Category: %s' % self.name


class BaseModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    image = models.ImageField()
    url = models.URLField(max_length=1000, null=True, blank=True)
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
    stock = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    categories = models.ManyToManyField(Category)


# class Variation(BaseModel):
#     product = ParentalKey(Product, related_name='product_variations', on_delete=models.CASCADE)
#     stock = models.IntegerField(blank=True, null=True)

class Wallet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    related_affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True, default=0)


class Receipt(models.Model):
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_amount = models.IntegerField(blank=True, null=True)
    affiliate_amount = models.IntegerField(blank=True, null=True)
    related_affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')


class Transaction(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    related_affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    Types = (
        ('a', 'Add'),
        ('m', 'Minus'),
    )
    types = models.CharField(max_length=2, choices=Types)
