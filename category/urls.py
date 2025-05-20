from django.urls import path
from . import views
from .views import CategoryList,CategoryDetail,CategoryUpdate,CategoryCreate,CategoryDelete
app_name = 'category'

urlpatterns = [
    path('list/',CategoryList.as_view() , name='category_list'),
    path('details/<int:pk>/', CategoryDetail.as_view(), name='category_details'),
    path('delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    path('add/', CategoryCreate.as_view(), name='category_add'),
    path('update/<int:pk>', CategoryUpdate.as_view(), name='category_update'),
]