from django.http import HttpResponse
from django.template import Template, Context 
from django.shortcuts import render
from productos.models import Productos


def login(request):
    return render(request,"views_html/register_new.html")

def respuesta(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, "static/views_html/productos.html", data)

def inicio(request):
    doc_externo = open("static/views_html/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)      

def registro(request):
    doc_externo = open("static/views_html/register_new.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def productos(request):
    doc_externo = open("static/views_html/productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def base(request):
    doc_externo = open("static/views_html/base.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)
