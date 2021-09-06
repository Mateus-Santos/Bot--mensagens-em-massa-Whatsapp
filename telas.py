# CRIADO POR MATEUS SANTOS DE JESUS.
# Instagram: teeusantos20
# Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210

import csv

from PySimpleGUI import PySimpleGUI as sg


class TelaPrincipal:

    # CRIADO POR MATEUS SANTOS DE JESUS.
    # Instagram: teeusantos20
    # Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210


    # Layout
    def __init__(self):
        file_types = [("csv (*.csv)", "*.csv")]
        sg.theme('GreenMono')
        layout = [
            [sg.FileBrowse('IMPORTAR ARQUIVO', file_types=file_types),
                sg.Text('Local arquivo:'),
                sg.Text('Número do País:'),
             ],
            [sg.Text('Enviar Mensagem:')
             ],
            [sg.Button('Enviar')]
        ]
        # Janela
        janela = sg.Window("ChamasBot - Version Alpha 1.0.0").layout(layout)
        self.janela = janela
        self.layout = layout

    def Iniciar(self):
        janela = tela.getJanela()
        layout = tela.getLayout()
        event, values = janela.read()

    def getJanela(self):
        return self.janela

    def getLayout(self):
        return self.layout


tela = TelaPrincipal()
tela.Iniciar()

# CRIADO POR MATEUS SANTOS DE JESUS.
# Instagram: teeusantos20
# Linkedin: https://www.linkedin.com/in/mateus-santos-095a53210