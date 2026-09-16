from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "categoria")
    search_fields = ("nombre", "precio")
    ordering = ("nombre",)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("estado", "cliente", "fecha",)
    search_fields = ("estado", "cliente", "fecha")
    ordering = ("cliente",)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "producto", "cantidad", "subtotal")
    search_fields = ("pedido",)
    ordering = ("pedido",)