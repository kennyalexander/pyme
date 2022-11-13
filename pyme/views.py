from django.http import HttpResponse
from django.template import Template, Context 
from django.shortcuts import render 


def login(request):
    return render(request,"views_html/register_new.html")

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)      

def seguimiento(request):
    doc_externo = open("static/views_html/seguir.html") 
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

def fundacion(request):
    doc_externo = open("static/views_html/donaciones.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def productos(request):
    doc_externo = open("static/views_html/resultado.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)         

def carrito(request):
    doc_externo = open("static/views_html/carrito.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()       
    documento = plt.render(ctx)
    return HttpResponse(documento)           