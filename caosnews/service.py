import requests
import json

def listar_juegos():
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def agregar_chiste(chiste,resp):
    url = "http://127.0.0.1:8000/api/lista_corta"
    body = {"chiste":chiste,"resp":resp}
    cabecera={"content-type":"application/json"}
    response = requests.post(url,json=body,headers=cabecera)
    return response.status_code

def lista_chiste():
    url = "http://127.0.0.1:8000/api/lista_corta"
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def listar_colab_nombre(nombre):
    url = "http://127.0.0.1:8000/api/obtenercolabnombre/"+nombre
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def listar_colab ():
    url = "http://127.0.0.1:8000/api/obtenerUsuarios"
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def listar_colab_rut (rut):
    url = 'http://127.0.0.1:8000/api/obtenercolab/'+rut
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    return data

def api_tiempo():
    url = "http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=xb9iuvi34l9z&v=3.0"
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    data2 = data['day']
    data3 = data2['1']
    return data3
