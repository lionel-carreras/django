from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


# Create your views here.
def index(request):
    
    return render(request, 'inicio/index.html')

def nosotros(request):
    return render(request, 'nosotros/index.html')

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos/index.html', context)

def contacto(request):
    return render(request, 'contacto/index.html')

def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})