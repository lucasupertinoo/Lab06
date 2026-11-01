import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        """ Legge tutti gli strumenti dal database e li mostra nella ListView """
        self._view.lista_strumenti.controls.clear()

        strumenti = self._model.get_strumenti()
        if strumenti is None:
            self._view.show_alert("❌ Errore di connessione al database")
            self._view.update()
            return

        if len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento presente nel deposito")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(str(strumento)))
        self._view.update()

    def cerca_strumenti(self, e):
        """ Cerca nel database gli strumenti del tipo inserito e li mostra nella ListView """
        self._view.lista_strumenti_ricerca.controls.clear()

        tipo = self._view.input_tipo_strumento.value
        if tipo is None or tipo.strip() == "":
            self._view.show_alert("Inserire il tipo di strumento da cercare")
            self._view.update()
            return

        tipo = tipo.strip()
        strumenti = self._model.cerca_strumenti_per_tipo(tipo)
        if strumenti is None:
            self._view.show_alert("❌ Errore di connessione al database")
            self._view.update()
            return

        if len(strumenti) == 0:
            self._view.show_alert(f"Nessuno strumento di tipo '{tipo}' trovato")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(strumento)))
        self._view.update()
