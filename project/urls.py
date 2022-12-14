"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from ejemplo.views import index, index_1, monstrar_familiares, BuscarFamiliar, AltaFamiliar, Home, Post, About, Contact
from blog.views import index_0

urlpatterns = [
    path('home/', Home),
    path('post/', Post),
    path('about/', About),
    path('contact/', Contact),
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('mostrar-notas/', index_1),
    path('blog/', index_0),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('panel-familia/', include('panel_familia.urls')),
]
