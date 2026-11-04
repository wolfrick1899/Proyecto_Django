from django.shortcuts import render
from .models import Estudiante

def pantalla(request):
    return render(request, 'inicio.html')

def inicio(request):

    if not Estudiante.objects.filter(documento="12345").exists():

        Estudiante.objects.create(
            documento="12345",
            nombre="Mike",
            apellido="Arias",
            edad=19
        )

    if not Estudiante.objects.filter(documento="3361612").exists():

        Estudiante.objects.create(
            documento="3361612",
            nombre="Logan",
            apellido="Mendez",
            edad=19
        )

    estudiantes = Estudiante.objects.all()

    return render(request, 'estudiantes.html', {
        'estudiantes': estudiantes
    })