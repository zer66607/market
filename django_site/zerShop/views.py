from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Category, Order, Product

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

class ProductCreate(UserPassesTestMixin, generic.CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'
    login_url = '/'
    
    def test_func(self): 
          return self.request.user.is_superuser

class ProductEdit(UserPassesTestMixin, generic.UpdateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'
    login_url = '/'

    def test_func(self): 
          return self.request.user.is_superuser

class ProductDelete(UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products')
    login_url = '/'

    def test_func(self): 
          return self.request.user.is_superuser

class OrderFormView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'product_order.html'
    success_url = reverse_lazy('order_success')
    fields = ['customer_name','customer_phone','customer_email']

    def form_valid(self, form):
        product = Product.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        form.instance.user = user
        form.instance.product = product
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=self.kwargs['pk'])
        return context

class OrderSuccessView(generic.TemplateView):
    template_name = 'order_success.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    context_object_name = 'sign'
