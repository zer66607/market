from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Product, Category, Order

# Create your views here.

class ProductList(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductDetail(generic.DetailView):
    template_name = 'product_detail.html'
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryDetail(generic.DetailView):
    template_name = 'categoty_detail.html'
    context_object_name = 'category'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductCreate(generic.CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'

class ProductEdit(generic.UpdateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'

class ProductDelete(generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products')

class OrderFormView(generic.CreateView):
    model = Order
    template_name = 'product_order.html'
    success_url = reverse_lazy('products')
    fields = ['customer_name','customer_phone']

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)