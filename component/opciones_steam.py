import PySimpleGUI as sg
from windows import opciones_steam
from component import steam_mas_jugados
from component import tipo_juegos
def start():
    """
    Lanza la ejecución de la ventana de opciones de Steam
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de opciones que capta los eventos al apretar una opcion
    """

    window = opciones_steam.build()

    while True:
    
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir","salir"):
            break
        if event=="-type-":
            tipo_juegos.start()
        if event== "-mas_jugados-":
            steam_mas_jugados.start()

    return window