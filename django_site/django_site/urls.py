"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zerShop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.ProductList.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category'),
    path('product/new/', views.ProductCreate.as_view(), name='product_new'),
    path('product/<int:pk>/edit/', views.ProductEdit.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/order/', views.OrderFormView.as_view(), name='product_order'),
    path('product/order_success/', views.OrderSuccessView.as_view(), name='order_success'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)