# api/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list_create, name='product-list-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),

]
