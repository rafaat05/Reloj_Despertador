import time

def configuracion_alarma():
    "Pide al usuario que seleccione una hora para que suena la alarma, se ejecuta al coincidir la hora local con la seleccionada"
    print("Configuracion de alarma")
    alarma_usuario=input("Seleccione cuando quiere que suene la alarma: ").strip()
    print("Alarma programada")

    while True:
        hora_actual=time.strftime("%H:%M")

        if hora_actual == alarma_usuario:
            #Salimos de la funcion devolviendo True
            return True
        time.sleep(1)