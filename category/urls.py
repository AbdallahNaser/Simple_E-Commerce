from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('list/', views.category_list, name='category_list'),
    path('details/<int:id>/', views.category_details, name='category_details'),
    path('delete/<int:id>/', views.category_delete, name='category_delete'),
    path('add/', views.category_add, name='category_add'),
]