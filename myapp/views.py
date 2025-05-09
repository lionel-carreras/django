from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

def index(request):
    msj =''
    if request.method == 'POST':
        name = request.POST.get('name','')
        if name:
            msj = f'Hola {name} esta es una respuesta desde el servidor'
            
        else:
            msj = 'No se ha ingresado un nombre'

    return render(request, 'myapp/index.html', {'msj': msj})
        

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/estudiante_detail.html', {'estudiante': estudiante})          

   

   
    
