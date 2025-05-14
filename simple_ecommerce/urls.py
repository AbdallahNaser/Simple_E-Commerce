from django.contrib import admin
from django.urls import path
from product.views import product_list
from category.views import category_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list, name='products'),
    path('categories/', category_list, name='categories'),
]
