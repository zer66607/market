from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, null=True)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name='products')
    image = models.ImageField(upload_to='pics', null=True)
    price = models.IntegerField(default=0)
    price_discounted = models.IntegerField(null=True, blank=True)
    colors = (
        ('black', 'Черный'),
        ('gray', 'Серый'),
        ('yellow', 'Желтый'),
        ('green', 'Зеленый'),
        ('red', 'Красный'),
        ('blue', 'Синий'),
    )
    color = models.CharField(max_length=30, choices=colors, null=True, blank=True)

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

class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete='CASCADE')
    product = models.ForeignKey('Product', on_delete='CASCADE')
    content = models.TextField('Отзыв')
    pub_date = models.DateTimeField('Дата добавления отзыва', default=datetime.now)
    status = models.BooleanField('Показывать отзыв', default=False)
    stars = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),        
    )
    rating = models.IntegerField('Рейтинг товара', choices=stars, default='5')

    def __str__(self):
        return self.content[0:200]

    def get_absolute_url(self):
        return reverse('product', args=[self.product.id])
    
