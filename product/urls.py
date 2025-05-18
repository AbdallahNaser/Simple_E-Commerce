from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('detail/<int:id>/', views.product_details, name='product_details'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:id>', views.product_edit, name='product_edit'),
]