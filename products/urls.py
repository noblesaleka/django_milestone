from django.urls import path
from . import views
from django.conf import settings

from django.views.static import serve

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('author/<author_id>/', views.author_detail, name='author_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]

