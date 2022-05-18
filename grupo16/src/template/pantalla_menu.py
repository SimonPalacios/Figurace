import random

import PySimpleGUI as Sg
from template.pantalla_jugar import jugar
from template.pantalla_crear_perfil import Login
from template.pantalla_configuracion import Settings


class MainMenu:

    def __init__(self):
        """ creamos la interfaz del menu de inicio
            instanciamos el loop de menu
            """
        self._window = self.crear_menu()
        self.loop()

    def crear_menu(self):

        nombre_menu = "menu inicio"
        layout = [[Sg.Button('Configuración', key="-settings-", size=(20, 2)),
                   Sg.Button('Jugar', key="-play-", size=(20, 2)), ],
                  [Sg.Button('Perfil', key='-user-', size=(20, 2)),
                   Sg.Button('Puntuaciones', key='-puntaje-',
                             size=(20, 2))],
                  [Sg.Button('Salir', key="-Exit-", size=(45, 2))]]
        ventana_menu = Sg.Window(nombre_menu, layout, size=(400, 150),
                                 finalize=True)
        return ventana_menu

    def loop(self):
        while True:
            event, values = self._window.read()
            print(f"  Evento: {event}, valores: {values}")

            match event:
                case Sg.WIN_CLOSED | "-Exit-":
                    break
                case "-play-":
                    self._window.hide()
                    jugar()
                    self._window.un_hide()
                case "-user-":
                    self._window.hide()
                    Login()
                    self._window.un_hide()
                case "-puntaje-":
                    print("tenemos que programar pantalla de puntajes")
                case "-settings-":
                    self._window.hide()
                    Settings()
                    self._window.un_hide()
        self._window.close()