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


#1.Gestion de carpeta url 
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
        #.strip--> uso para aeliminar espacios y saltos de linea
        url=url.strip()
        lista_url.append(url)
    print(lista_url)

#2.Gestion del tiempo
#pedir al usuario la hora exacta que quiere que suene la alarma
#funcion time.sleep()->pausa la ejecucion del programa
#time.strftime()->obtiene la hora y el minuto actual(%H:%M)

#Peticion de alarma al usuario
print("Configuracion de alarma")
alarma_usuario=input("Seleccione cuando quiere que suene la alarma: ").strip()#evita fallos por espacios
print("Alarma programada")
while True:
    #variable con la hora actual
    hora_actual=time.strftime("%H:%M")

    #condicional para controlar cuando las horas coinciden
    if hora_actual != alarma_usuario:
        #El programa espera un segundo para evitar fallos
        time.sleep(1)
    else:
        #si la hora coincide salimos del programa u ejecutamos
        break

#3.Seleccion aleatoria de url en lista_url, busqueda y ejecucion de url por el navegador

#seleccion aleatoria en la lista_url
url_seleccionada=random.choice(lista_url)
#apertura de la url
#Ejecuta el proceso de apetura directamente desde las herramientas windows
os.system(f"powershell.exe Start-Process '{url_seleccionada}'")
