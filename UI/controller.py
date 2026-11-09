import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown_genere(self):
        generi=self._model.lista_generi
        self._view.dropdown_genere.options.clear()
        self._view.dropdown_genere.options.append(ft.dropdown.Option(key=str(None), text="Nessun filtro"))
        if generi:
            for genere in generi:
                self._view.dropdown_genere.options.append(ft.dropdown.Option(key=str(genere), text=str(genere)))
            return self._view.dropdown_genere
        else:
            return self._view.show_alert("Errore nel caricamento generi.")

    def popola_dropdown_biblioteca(self):
        biblioteche=self._model.lista_biblioteche
        self._view.dropdown_biblioteca.options.clear()
        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(key=str(None), text="Nessun filtro"))
        if biblioteche:
            for biblioteca in biblioteche:
                self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(key=str(biblioteca.id), text= str(biblioteca.nome)))
            return self._view.dropdown_biblioteca
        else:
            return self._view.show_alert("Errore nel caricamento biblioteche.")


    # CALLBACKS DROPDOWN
    def on_change_genere(self,e):
        valore=e.control.value
        self.genere_selezionato=valore
        return self.genere_selezionato

    def on_change_biblioteca(self,e):
        valore=e.control.value
        self.biblioteca_selezionata=valore
        return self.biblioteca_selezionata


    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        libri= self._model.get_libri_filtrati(str(self.biblioteca_selezionata),str(self.genere_selezionato))
        self._view.libri_filtrati.controls.clear()
        if libri is None:
            return self._view.show_alert("Errore di connessione al database.")
        elif len(libri) == 0:
            return self._view.show_alert("Nessun libro trovato per i criteri selezionati")
        else:
            for libro in libri:
                self._view.libri_filtrati.controls.append(ft.Text(f"{libro}"))
            return self._view.libri_filtrati

