from django.contrib import admin
from .models import Producto, Cliente, Mesero, Factura, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Mesero)
admin.site.register(Factura)
