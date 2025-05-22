# api/urls.py
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'productsV', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),

    path('products/', product_list_create, name='product-list-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/', ProductDetailUpdateDeleteView.as_view(), name='product-detail-update-delete'),

]
