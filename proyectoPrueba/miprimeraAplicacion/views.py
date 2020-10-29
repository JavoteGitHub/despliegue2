from django.shortcuts import render
from django.http import HttpResponse
from .models import TejidoMama
# Create your views here.
print(">>>>>>>>>>>>>>>>>>>>>> Ejecutando <<<<<<<<<<<<<<<<<<<<<<<<")
def miInicio(request):    
    return render(request, 'miprimeraAplicacion/inicio.html')   

def informacion(request):    
    #return HttpResponse ("<h2>HOLA MUNDO ESTA ES MI PRIMERA PRUEBA</h2>") PARA AGREGAR PDF    
    return render(request, 'miprimeraAplicacion/informacion.html')   

def causas(request):
    return render(request, 'miprimeraAplicacion/causas.html')

def alumno(request):
    return render(request, 'miprimeraAplicacion/alumno.html')

def apoyo(request):
    return render(request, 'miprimeraAplicacion/apoyo.html')

def contacto(request):
    return render(request, 'miprimeraAplicacion/contacto.html')

def cdi(request):
    return render(request, 'miprimeraAplicacion/cdi.html')

def cmm(request):
    return render(request, 'miprimeraAplicacion/cmm.html')

def camm(request):
    return render(request, 'miprimeraAplicacion/camm.html')

def bdd(request):
    lista = TejidoMama.objects.all()
    return render(request, 'miprimeraAplicacion/informacion.html', {'misdatos': lista})



    