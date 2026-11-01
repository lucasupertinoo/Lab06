import flet as ft
# Anche l'alert è universale e va bene in ogni programma nella sua struttura globale

class AlertManager:
    def __init__(self, page: ft.Page):
        self._page = page
        self._alert_dialog = ft.AlertDialog(
            title=ft.Text(""),
            actions=[ft.TextButton("OK", on_click=self.close)]
        )

    def show_alert(self, message: str):
        self._alert_dialog.title.value = message
        if self._alert_dialog.open:
            self._page.update()
        else:
            self._page.show_dialog(self._alert_dialog)

    def close(self, e):
        self._page.pop_dialog()
