from django.contrib import admin
from django.urls import path
from pedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.productos, name="productos"),
    path('test/', views.test, name="test"),
    path('registro/', views.registro, name="registro")
]
