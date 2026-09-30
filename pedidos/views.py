from django.shortcuts import render, redirect
from .models import Producto, Categoria

from .serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def productos (request):
    productos = Producto.objects.all()  

    return render (request,
                   "pedidos/productos.html",
                   {"productos":productos})
def test(request):
    return render (request, "pedidos/prueba.html")

def registro(request):
    if request.method =="POST":
        
        Producto.objects.create(
            nombre=request.POST["nombre"], 
            precio=request.POST["precio"], 
            categoria = Categoria.objects.get(id = request.POST["categoria"])
        )
        return redirect ('/')

    return render (request,"pedidos/registro.html")

def editar(request):
    productos = Producto.objects.all()
    return render (request,"pedidos/editar.html", {"productos":productos})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        
        producto.nombre = request.POST["nombre"]
        producto.precio = request.POST["precio"]
        producto.categoria = Categoria.objects.get(id = request.POST["categoria"])
        producto.save()
        return redirect("editar")

    return render (request,"pedidos/editar_producto.html", {"producto":producto, "categorias":categorias})

@api_view(["GET"])
def api_productos(request):
    productos = Producto.objects.all()

    datos = ProductoSerializer(productos, many=True)  
    return  Response(datos.data)
        