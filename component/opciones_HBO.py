import PySimpleGUI as sg
from windows import opciones_HBO
from windows import segun_anio
from component import segun_anio
def start():
    """
    Lanza la ejecución de la ventana de opciones de HBO
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de opciones que capta los eventos al apretar una opcion
    """

    window = opciones_HBO.build()

    while True:
    
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event=="-agregar_anio-":
            segun_anio.start()
    
    return window
