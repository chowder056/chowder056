from caosnews.forms import caosnewsForm
from django.http import request
from django.shortcuts import render,redirect
from .models import caosnews
from .service import *

def Home(request):
    #esnseñar contenido de la BD
    pagina1= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'pagina1.html',{'caosnews':pagina1,'clima':clima})
    
def Registro(request):
    pagina1= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'registro.html',{'caosnews':pagina1,'clima':clima})

def Pandemia(request):
    pandemia= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'cate.pandemia.html',{'caosnews':pandemia,'clima':clima})

def Deporte(request):
    Deporte= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'cate.deportes.html',{'caosnews':Deporte,'clima':clima})

def Internacional(request):
    Internacional= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'cate.internacional.html',{'caosnews':Internacional,'clima':clima})

def finanzas(request):
    finanzas= caosnews.objects.all()
    clima = api_tiempo()
    return render(request, 'cate.finanzas.html',{'caosnews':finanzas,'clima':clima})

def comunas_cuarentena(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'comunas en cuarentena.html',data)

def china_dosis(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'china estudia aumentar dosis.html',data)

def director_sinovac(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'director sinovac.html',data)

def tercer_retiro(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, '3er retiro.html',data)

def anf_denuncia(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'anf denuncia a fiscalia.html',data)

def bono_covid(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'bono covid abril.html',data)

def coronavac(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'coronavac.html',data)
    
def iran_acusa_israel(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'iran acusa a israel.html',data)

def roja_femenina(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'roja femenina.html',data)

def sinovac(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'sinovac.html',data)

def suspendido_lluvia(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'suspendido por lluvia.html',data)

def contactanos(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'contactanos.html',data)

def balance(request):
    clima = api_tiempo()
    data = {'clima':clima}
    return render(request, 'balance.html',data)

#def registro(request):
 #   return render(request, 'registro.html') 

def registro(request):
    clima = api_tiempo()
    caosU= caosnews.objects.all()
    if request.method == "POST":
            if 'Agregar' in request.POST:  
                form = caosnewsForm(request.POST)  
                if form.is_valid():  
                    try:  
                        form.save()  
                        return redirect('/registro')  
                    except:  
                        pass
            if 'Editar' in request.POST:
                cas = caosnews.objects.get(id=request.POST['id'])
                form = caosnewsForm(request.POST, instance=cas)
                if form.is_valid:
                    try:
                        form.save()
                        return redirect('/registro')
                    except:
                        pass
            if 'Eliminar' in request.POST:
                fora = caosnews.objects.get(id=request.POST['id'])  
                fora.delete()  
                return redirect('/registro')

    else:  
        form = caosnewsForm()  
    return render(request,'registro.html',{'caosU':caosU,'form':form,'clima':clima})

def freetogame (request):
    clima = api_tiempo()
    data = {'games' : listar_juegos(),'clima':clima}
    return render(request,'freetogame.html',data)

def subida (request):
    clima = api_tiempo()
    if request.method == "POST":
        chiste = request.POST['chiste']
        resp = request.POST['resp']
        agregar_chiste(chiste,resp)
        return redirect(to="chiste/")
    return render(request, 'subida.html', {'clima':clima})

def listachiste (request):
    clima = api_tiempo()
    data = {'chistes' : lista_chiste(),'clima':clima}
    return render(request,'lista_chiste.html',data)

def buscarColaborador(request):
    clima = api_tiempo()
    data = {'colaboradores': listar_colab(),'clima':clima}
    return render(request, 'buscar colaborador.html',data)
    
def buscarColaboradorNombre(request):
    clima = api_tiempo()
    if request.method == "POST":
        nombre = request.POST['nombre']
        data = {'colaboradores': listar_colab_nombre(nombre),'clima':clima}
    
    return render(request, 'buscarColaboradorNombre.html',data)

def buscarColaboradorRut(request):
    clima = api_tiempo()
    if request.method == "POST":
        rut = request.POST['rut']
        data = {'colaboradores': listar_colab_rut(rut),'clima':clima}
    
    return render(request, 'buscarColaboradorRut.html',data)





    



#def NuevoNombre(request):
 #   if request.method == "POST"

    