import PySimpleGUI as sg

def build():
    """
    Construye la ventana de buscar juegos segun lo ingresado: gratis o pagos
    """
    layout = [[sg.Text('Ingrese gratis o pagos para buscar'), sg.Input(key='-type-')],
             [sg.Button('aceptar'),sg.Button('salir')]]
             
    board = sg.Window('Guardar los juegos gratis o pagos').Layout(layout)

    return board