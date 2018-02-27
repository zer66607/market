from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, null=True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name='products')
    image = models.ImageField(upload_to='pics', null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title