import PySimpleGUI as sg
from windows import segun_anio
import csv
import json
def start():
    """
    Lanza la ejecución de la ventana del año ingresado
    """
    window = loop()
    window.close()

def write_json(data, filename='/home/alumno/Documentos/entregas/teoria/peliculas.json'):
    """esta funcion agrega  peliculas al archivo"""
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def loop():
    """
    Loop de la ventana que buscará segun el año ingresado y escribirá en el archivo jSon
    """

    window = segun_anio.build()

    while True:
    
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event== "aceptar":
            anio=values['-anio-']
            archivo = open('/home/alumno/Documentos/entregas/teoria/HBO_MAX_Content.csv', "r")
            csvreader = csv.reader(archivo, delimiter=',')
            print(f'se cargaran los titulos del año:  {anio}') 
            cant=0
            for linea in csvreader:
                if(anio==linea[2]):
                    cant+=1
                    titulo=linea[0]
                    tipo=linea[1]
                    anio=linea[2]
                    rating=linea[3]
                    print('titulo:', titulo ,'tipo: ' ,  tipo  ,'año: ', anio  ,'rating:', rating )
                    with open('/home/alumno/Documentos/entregas/teoria/peliculas.json',"r+") as json_file:
                        data = json.load(json_file)
                        temp = data['info_peliculas']
                        # objeto python que quiero agregar
                        y = {'-titulo pelicula-':titulo,
                            '-tipo de pelicula-':tipo,
                            '-anio-':anio,
                            'rating':rating
                            }
                        # agrego nueve pelicula al archivo json
                        temp.append(y)
                        #llamo a funcion que escribe
                        write_json(data)
            if (cant==0):
                print(f"en el {anio}  no se registran peliculas, por favor intente con otro año")  
            break
    return window