from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return HttpResponse('<font color="green"><h1>Hola Mundo con Django</h1></font>')

def pagina(request):
    return render(request, 'pagina.html')