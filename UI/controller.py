import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""

        self._model.get_nodi()
        self._model.get_archi()

        n_nodi = self._model.numero_nodi()
        n_archi = self._model.numero_archi()
        min, max = self._model.peso_massimo_minimo()

        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato corretamente"
                                                          f" Numero di nodi : {n_nodi}"
                                                          f" Numero di archi : {n_archi}"
                                                          f" Peso minimo : {min}"
                                                          f" Peso massimo : {max}"))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""

        soglia = self._view.txt_name.value

        if not soglia:
            self._view.show_alert("Inserire un valore per la soglia")
            return

        try:
            soglia = float(soglia)
        except ValueError:
            self._view.show_alert("Inserire un valore numerico per la soglia")
            return

        min, max = self._model.peso_massimo_minimo()
        if not min <= soglia <= max:
            self._view.show_alert("Inserire un valore compreso tra massimo e minimo per la soglia")
            return

        minori, maggiori = self._model.archi_soglia(soglia)

        self._view.lista_visualizzazione_2.controls.clear()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f" Soglia impostata {soglia}"
                                                                   f" Numero archi minori : {minori}"
                                                                   f" Numero archi maggiori : {maggiori}"))
        self._view.update()

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""

        soglia = self._view.txt_name.value
        if not soglia:
            self._view.show_alert("Inserire un valore per la soglia")
            return

        soglia = float(soglia)

        cammino_ottimo, peso_massimo = self._model.cerca_cammino_massimo(soglia)

        if not cammino_ottimo:
            self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Nessun cammino trovato"))
        else:
            cammino_mappa = "->".join(map(str, cammino_ottimo))
            self._view.lista_visualizzazione_3.controls.clear()
            self._view.lista_visualizzazione_3.controls.append(ft.Text(f" Cammino di peso massimo trovato {soglia}"
                                                                   f" Peso totale {peso_massimo}"
                                                                   f" Nodi attraversati {len(cammino_ottimo)} {cammino_mappa}"))

        self._view.update()