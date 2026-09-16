from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def productos (request):
    productos = Producto.objects.all()  

    return render (request,
                   "pedidos/productos.html",
                   {"productos":productos})
def test(request):
    return render (request, "pedidos/prueba.html")

def registro(request):
    return render (request,"pedidos/registro.html")