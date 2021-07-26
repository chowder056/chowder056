from collections import namedtuple
from django.contrib import admin
from django.urls import path, include
from .views import   *
from .views import Home,Registro


urlpatterns = [
    path('',Home, name='Home'),
    path('pandemia/', Pandemia, name='pandemia' ),
    path('deporte/', Deporte, name='deporte' ),
    path('internacional/', Internacional, name='internacional'),
    path('finanzas/', finanzas, name='finanzas'),
    path('comuna_cuarentena/', comunas_cuarentena, name='comuna_cuarentena'),
    path('china_dosis/', china_dosis, name='china_dosis'),
    path('director_sinovac/', director_sinovac, name='director_sinovac'),
    path('tercer_retiro/', tercer_retiro, name='tercer_retiro'),
    path('anf_denuncia/', anf_denuncia, name='anf_denuncia'),
    path('bono_covid/', bono_covid, name='bono_covid'),
    path('coronavac/', coronavac, name='coronavac'),
    path('iran_acusa_israel/', iran_acusa_israel, name='iran_acusa_israel'),
    path('roja_femenina/', roja_femenina, name='roja_femenina'),
    path('sinovac/', sinovac, name='sinovac'),
    path('suspendido_lluvia/', suspendido_lluvia, name='suspendido_lluvia'),
    path('registro/',registro,name= 'registro'),
    path('juegosf2p/',freetogame,name="juegosf2p/"),
    path('contactanos/',contactanos,name="contactanos/"),
    path('balance/',balance,name="balance/"),
    path('chiste/', subida, name='chiste/'),
    path('buscarColaborador',buscarColaborador, name="buscarColaborador/"),
    path('buscarColaboradorNombre',buscarColaboradorNombre, name='buscarColaboradornNombre/'),
    path('buscarColaboradorRut',buscarColaboradorRut, name='buscarColaboradornRut/'),
    path('lista_chiste/',listachiste, name='lista_chiste/'),
]

#urlpatterns = [
 #   path('',views.Pandemia, name='Pandemia')
      
#]


#def Pandemia(request):
    #esnseñar contenido de la BD
 #   pandemia= caosnews.objects.all()
  #  return render(request, 'cate.pandemia.html',{'caosnews':pandemia})