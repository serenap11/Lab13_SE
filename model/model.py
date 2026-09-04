import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.cromosomi = []
        self.connessioni = []
        self.G = nx.DiGraph()

    def get_nodi(self):
        dati = DAO.get_cromosomi()
        self.cromosomi.clear()
        self.cromosomi = [row["cromosoma"] for row in dati]

        self.G.clear()
        self.G.add_nodes_from(self.cromosomi)

        return self.cromosomi

    def get_archi(self):

        dati = DAO.get_connessioni()

        pesi = {}

        for d in dati:
            arco = (d["c1"], d["c2"])
            correlazione = d["correlazione"]
            if arco in pesi:
                pesi[arco] += correlazione
            else:
                pesi[arco] = correlazione

        for (c1, c2), peso in pesi.items():
            self.G.add_edge(c1, c2, weight=peso)

        return pesi

    def numero_nodi(self):
        return self.G.number_of_nodes()

    def numero_archi(self):
        return self.G.number_of_edges()

    def peso_massimo_minimo(self):

        pesi = [dati["weight"] for u, v, dati in self.G.edges(data=True)]
        if not pesi:
            return 0, 0
        return min(pesi), max(pesi)

    def archi_soglia(self, soglia):

        archi_minori = 0
        archi_maggiori = 0

        for u, v, p in self.G.edges(data=True):
            peso = p["weight"]
            if peso < soglia:
                archi_minori += 1
            if peso > soglia:
                archi_maggiori += 1

        return archi_minori, archi_maggiori

    def cerca_cammino_massimo(self, soglia):

        self.best_cammino = []
        self.best_peso = 0

        for nodo_partenza in self.G.nodes():
            self.ricorsione([nodo_partenza], 0, soglia)

        return self.best_cammino, self.best_peso

    def ricorsione(self, parziale, peso, soglia):

        nodo_corrente = parziale[-1]
        valido = False

        for vicino in self.G.successors(nodo_corrente):
            peso_arco = self.G[nodo_corrente][vicino]["weight"]

        if peso > soglia and vicino not in parziale:
            valido = True

            parziale.append(vicino)
            self.ricorsione(parziale, peso + peso_arco, soglia)

            parziale.pop()

        if not valido:
            if peso_arco > self.best_peso:
                self.best_peso = peso_arco
                self.best_cammino = parziale





if __name__ == "__main__":
    model = Model()
    nodi = model.get_nodi()
    print(nodi)
    archi = model.get_archi()
    print(archi)