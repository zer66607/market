from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import Product

class IndexView(generic.ListView):

    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
