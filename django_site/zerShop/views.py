from django.shortcuts import render
from django.views import generic

from .models import Product, Category

# Create your views here.

class ProductList(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 6
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context

class CategoryDetail(generic.DetailView):
    template_name = 'categoty_detail.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context

class CategoryList(generic.ListView):
    template_name = 'category_list.html'
    context_object_name = 'categorys'
    model = Category