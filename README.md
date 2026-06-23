# Reloj despertador.

Herramienta monitoriza la hora del sistema en tiempo real, al alcanzar la hora configurada por el usuario, selecciona una cancion de forma aleatoria desde una lista personalizada y la reproduce abriendo el navegador web automaticamente.


## Arquitectura del proyecto

- **Inicio** el programa lee las variables de entorno.

- **Carga de datos**: El modulo lista_archivos_url.py accede a url.txt para cargar las opciones de memoria.

- **Bucle de tiempo**: Un ciclo continuo en configuracion.py comparando la hora actual con la seleccionada por el usuario.

- **Ejecucion**: el modulo ejecutar_url.py selecciona de manera aleatoria el enlace url y abrir el navegador.


## Estructura del proyecto

.
├── CHANGELOG.md
├── README.md
├── TODO.md
├── cliff.toml
├── pyproject.toml
├── requirements.txt
└── src
    ├── main.py
    ├── test.py
    ├── url.txt
    └── utils
        ├── __init__.py
        ├── configuracion.py
        ├── ejecutar_url.py
        └── lista_archivos_url.py


## Instalacion

- git clone 
- cd Reloj_Despertador
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt


## Uso

Una vez instalado situarse en src/ y ejecutar en la terminal: python main.py

El programa se ejecutara y guiara en el proceso:

1. Solicitara al usuario que introudzca la hora a la que quiere que suene la alarma

2. Comparará la hora con la actual en un bucle hasta que ambas coincidan

3. Abrirá el navegador de la url seleccionada aleatoriamente

El programa tiene url introducidas inicialmente en el archivo url.txt, si quiere añadir alguna seleccione este archivo e introduzca una por linea
 

## Tecnologia utilizada

- Python3
- time: comparacion del tiempo actual con el seleccionado por el usuario
- os: ruta a archivo.txt de las url asi como seleccion de powershell de windows para la ejecucion de apertura del navegador
- random: eleccion aleatoria de url de la lista