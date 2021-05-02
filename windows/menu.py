import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú de de la actividad
    """
    layout = [[sg.Text('¿SOBRE QUÈ DATOS ANALIZAMOS ?')],
             [sg.Button('HBO', size=(50, 2), key="-HBO-")],
             [sg.Button('Salir', size=(50, 2), key="-exit-")]]

    board = sg.Window('Menu de inicio').Layout(layout)

    return board