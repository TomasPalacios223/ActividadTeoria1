import PySimpleGUI as sg

from windows import menu
from component import opciones_HBO

def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    window = menu.build()

    while True:
    
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event== "-HBO-":
            opciones_HBO.start()
        if event == "--":
            pass
    return window
