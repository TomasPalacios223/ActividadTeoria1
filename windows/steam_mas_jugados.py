import PySimpleGUI as sg

def build():
    """
    Construye la ventana de informar imprimir juegos mas jugados
    """
    layout = [[sg.Text('Se imprimiran los 4 juegos mas jugados')],
             [sg.Button('aceptar'),sg.Button('salir')]]
             
    board = sg.Window('Aviso').Layout(layout)

    return board