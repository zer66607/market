from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

class IndexView(generic.ListView):
    
    template_name = 'products_list.html'
    context_object_name = 'zerShop'
    model = Product

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product