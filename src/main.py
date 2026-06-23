#miplementacion de todas las funcionalidades del proyecto en ub codigo limpio
#Primero la creacion de una lista donde añadir las url
#2 configuracion de la hroa de la alarma por el usuario
#3 ejecucion de la alarma con la url seleccionada aleatoriamente

print("Reloj despertador.")
# En main.py
from utils import gestion_url, configuracion_alarma, ejecutar_alarma

# creaciond de lista
lista= gestion_url()

#configuracion de alarma.
seleccion=configuracion_alarma()

#ejecucion
output=ejecutar_alarma(lista)