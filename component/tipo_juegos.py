import PySimpleGUI as sg
from windows import tipo_juegos
import csv
import json
def start():
    """
    Lanza la ejecución de la ventana de la busqueda de juegos 
    """
    window = loop()
    window.close()

def write_json(data, filename='/home/alumno/Documentos/entregas/teoria/juegos.json'):
    """esta funcion agrega  juegos al archivo"""
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def loop():
    """
    Loop de la ventana que buscará segun el año ingresado y escribirá en el archivo jSon
    """

    window =tipo_juegos.build()

    while True:
    
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event== "aceptar":
            j=values['-type-']
            archivo = open('/home/alumno/Documentos/entregas/teoria/steam-200.csv', "r")
            csvreader = csv.reader(archivo, delimiter=',')
            print(f'se cargaran los juegos de tipo  {j}') 
            j=j.lower()
            if(j=='gratis'):
                j='play'
            elif(j=='pagos'):
                j='purchase'
            for linea in csvreader:
                if(j==linea[2]):
                    titulo=linea[1]
                    idUsuario=linea[0]
                    horas_juego=linea[3]
                    tipo_juego=linea[2]
                    print('titulo:', titulo ,'idUsuario ' , idUsuario  ,'horas_juego: ', horas_juego  ,'tipo_de_juego:', tipo_juego )
                    with open('/home/alumno/Documentos/entregas/teoria/juegos.json',"r+") as json_file:
                        data = json.load(json_file)
                        temp  = data['info_juegos']
                        # objeto python que quiero agregar
                        y = {'-titulo del juego-':titulo,
                             '-id de usuario-':idUsuario,
                             '-horas_de_juego-':horas_juego,
                             'tipo_de_juego':tipo_juego
                            }
                        # agrego nuevo juego a  json
                        temp.append(y)
                        #llamo a funcion que escribe
                        write_json(data) 
            if(j!='play' and j!='purchase') :
                print('por favor asegurese de ingresar de la siguiente manera: GRATIS O PAGOS')
            break
    return window