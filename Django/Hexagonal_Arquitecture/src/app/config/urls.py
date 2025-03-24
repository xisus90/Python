from django.contrib import admin
from django.urls import path
from src.app.infrastructute.routers.product_router import ProductRootView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', ProductRootView.as_view(), name='product_root'),
]
