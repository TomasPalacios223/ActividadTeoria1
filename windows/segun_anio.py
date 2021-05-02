import PySimpleGUI as sg

def build():
    """
    Construye la ventana de buscar titulo segun el año
    """
    layout = [[sg.Text('Ingresar año de pelicula a buscar'), sg.Input(key='-anio-')],
             [sg.Button('aceptar'),sg.Button('salir')]]
             
    board = sg.Window('Guardar las peliculas del año ingresado').Layout(layout)

    return board