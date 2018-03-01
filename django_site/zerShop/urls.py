from django.urls import path, include
from zerShop import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='product'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category'),
    path('product/new/', views.ProductCreate.as_view(), name='product_new'),
    path('product/<int:pk>/edit/', views.ProductEdit.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/order/', views.OrderFormView.as_view(), name='product_order'),
    path('product/order_success/', views.OrderSuccessView.as_view(), name='order_success'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
]