from django.urls import path, include
from zerShop import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('<int:pk>', views.ProductDetail.as_view(), name='product'),
    path('<int:pk>/edit/', views.ProductEdit.as_view(), name='product_edit'),
    path('<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('<int:pk>/order/', views.OrderFormView.as_view(), name='product_order'),
    path('<int:pk>/review/', views.AddReviewView.as_view(), name='add_review'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('new/', views.ProductCreate.as_view(), name='product_new'),
    path('order_success/', views.OrderSuccessView.as_view(), name='order_success'),
]