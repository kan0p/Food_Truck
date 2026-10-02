from django.contrib import admin
from django.urls import path
from pedidos import views
from pedidos.viewsets import ProductoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/v2/producto", ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.productos, name="productos"),
    path('test/', views.test, name="test"),
    path('registro/', views.registro, name="registro"),
    path('editar/',views.editar, name="editar"), 
    path('editar/<int:id>',views.editar_producto, name="editar_producto") ,
    
    path('api/v1/productos', views.api_productos, name="api_productos")
] + router.urls
