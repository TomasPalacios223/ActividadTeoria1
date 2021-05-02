import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú de opciones de HBO
    """
    layout = [[sg.Button('Buscar segun juegos gratis o pagos', size=(50, 2), key="-type-")],
             [sg.Button('Salir', size=(50, 2), key="-exit-")]]

    board = sg.Window('Menu de opciones de STEAM').Layout(layout)

    return board