"""proyectoPrueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miprimeraAplicacion import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.miInicio, name='inicio'),
    path('informacion/',views.informacion,name='informacion'),    
    path('causas/',views.causas,name='causas'),    
    path('alumno/', views.alumno,name='alumno'),
    path('apoyo/', views.apoyo,name='apoyo'),
    path('contacto/', views.contacto,name='contacto'),
    path('cdi/', views.cdi,name='cdi'),
    path('cmm/', views.cmm,name='cmm'),
    path('camm/', views.camm,name='camm'),
    #path('informacion', views.bdd,name='informacion'),
]
