from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, null=True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name='products')
    image = models.ImageField(upload_to='pics', null=True)
    price = models.IntegerField(default=0)
    price_discounted = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', args=[str(self.id)])

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

class Order(models.Model):
    product = models.ForeignKey('Product', on_delete='CASCADE')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete='CASCADE', null=True)

    def __str__(self):
        return self.customer_email
