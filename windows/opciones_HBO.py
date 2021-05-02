import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú de opciones de HBO
    """
    layout = [[sg.Button('Buscar segun año ingresado', size=(50, 2), key="-agregar_anio-")],
             [sg.Button('Salir', size=(50, 2), key="-exit-")]]

    board = sg.Window('Menu de opciones de HBO').Layout(layout)

    return board