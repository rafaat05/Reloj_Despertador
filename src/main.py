from utils import gestion_url, configuracion_alarma, ejecutar_alarma

if __name__ == "__main__":
    print("Reloj despertador.")

    # creacion de lista
    lista= gestion_url()

    #configuracion de alarma si lista > 0
    if lista>0:

        seleccion=configuracion_alarma()
    else:
        print("Lista de seleccion de url vacia.")
        quit

    #ejecucion
    output=ejecutar_alarma(lista)
