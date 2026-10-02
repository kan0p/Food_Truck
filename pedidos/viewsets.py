from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# clase para Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

