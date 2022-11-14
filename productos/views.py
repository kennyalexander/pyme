from django.shortcuts import render
from .models import Productos

def resultado(request):
    productos = Productos.objects.all()
    contexto = {'listadoProductos':productos}
    return render(request,"static/views_html/productos.html",contexto)