#libreria gestion de fechas
import datetime
#libreria buscador web
import webbrowser
#libreria gestion del tiempo
import time
#libreria eleccion aleatoria
import random
#libreria os-> geston de sistema
import os

#creacion de lista_url
lista_url=[]

#Averiguar la carpeta con el nombre del script .py
direct_actual=os.path.dirname(__file__)

#Union de la carpeta con el nombre del archivo txt
ruta_correcta=os.path.join(direct_actual, 'url.txt')

#operativa de lectura y adicion de url a lista_url
#Uso la variable ruta_correcta para señalar el archivo que quiero usar
with open(ruta_correcta) as archivo_url:
    urls =archivo_url.readlines()
    for url in urls:
        url=url.strip()
        lista_url.append(url)
    print(lista_url)

