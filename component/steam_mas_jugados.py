from windows import steam_mas_jugados
import csv
import requests
import collections
import PySimpleGUI as sg
import json


def write_json(data, filename='/home/alumno/Documentos/entregas/teoria/mas_jugados.json'):
    """esta funcion agrega  los juegos al archivo"""
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def start():
    """
    Lanza la ejecución de la ventana busqueda de los 10 mas jugados
    """
    window = loop()
    window.close()



def loop():
    """
    Loop de la ventana que buscará los mas jugados y los guardará en Json
    """

    window =steam_mas_jugados.build()

    while True:
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event== "aceptar":
            archivo = open('/home/alumno/Documentos/entregas/teoria/steam-200.csv', "r")
            csvreader = csv.reader(archivo, delimiter=',')
            reader = csv.reader(csvreader)
            top4= collections.Counter()
            reader=filter(lambda columna: columna[2]=='play',csvreader )
            for columna in reader:
                top4[(columna[1])]= float (columna[3])
            juegos_maximos_json=(top4.most_common(4))
            write_json(juegos_maximos_json)
            print("los cuatro juegos mas jugados son:")
            print(juegos_maximos_json)
            break
    return window