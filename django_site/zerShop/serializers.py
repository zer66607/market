from rest_framework import serializers
from .models import Product, Category, Order, Review

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'