from category.views import CategoryList
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CategoryList.as_view()),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('account/', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
