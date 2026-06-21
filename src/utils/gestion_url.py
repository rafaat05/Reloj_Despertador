import os


def gestion_url():
    "Creacion de la lista de las url utilizando archivo.txt-> url.txt"
    lista_url=[]

    direct_actual=os.path.dirname(__file__)
    ruta_correcta=os.path.join(direct_actual, 'url.txt')

    with open(ruta_correcta) as archivo_url:
        urls =archivo_url.readlines()
        for url in urls:
            url=url.strip()
            lista_url.append(url)
    return (lista_url)