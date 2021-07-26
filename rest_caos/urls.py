from django.contrib import admin
from django.urls import path, include
from . import views 
from caosnews.models import caosnews



urlpatterns = [
    path('lista_corta',views.lista_corta,name="lista_corta"),
    path('detalle_corta/<id>',views.detalle,name="detalle_corta"),
    path('obtenerUsuarios',views.ver_todo, name="ver_todo"),
    path('obtenercolab/<rut>',views.buscar_colab, name="buscar_colab"),
    path('obtenercolabnombre/<nombre>',views.buscar_colab_nombre, name="buscar_colab_nombre")
]