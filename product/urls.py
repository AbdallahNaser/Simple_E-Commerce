from django.urls import path
from . import views
from .views import *
app_name = 'product'

urlpatterns = [

    path('list/', views.product_list, name='product_list'),
    path('list/', views.product.as_view(), name='products'),
    path('detail/<int:id>/', views.product_details, name='product_details'),
    #path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('delete/<int:id>/', views.productdelete.as_view(), name='productclassdelete'),
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:id>', views.product_edit, name='product_edit'),
]