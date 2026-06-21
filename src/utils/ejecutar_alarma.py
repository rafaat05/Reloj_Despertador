
import random
import os


def ejecutar_alarma(lista_url):
    "Seleccion aleatoria de url en lista_url, busqueda y ejecucion de url por el navegador"
    print("HORA DE DESPERTARSE")

    url_seleccionada=random.choice(lista_url)
    #apertura de la url
 
    #Ejecuta el proceso de apetura directamente desde las herramientas windows
    os.system(f"powershell.exe Start-Process '{url_seleccionada}'")
