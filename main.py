import flet as ft

from model.model import DepositoStrumenti
from UI.view import View
from UI.controller import Controller

# Nel main importo flet, model, controller e view

'''
DA ESEGUIRE
'''

# Chiamo le varie funioni presenti nei vari file per settare controller, pagina, vista, interfaccia e model e poi runno
def main(page: ft.Page):
    my_model = DepositoStrumenti("Deposito Strumenti Musicali", "Alessandro Visconti")
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.run(main)
