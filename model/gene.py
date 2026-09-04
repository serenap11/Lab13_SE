from dataclasses import dataclass

@dataclass
class Gene:
    id : str
    funzione : str
    essenziale : str
    cromosoma : int

    def __str__(self):
        return f"{self.id} : funzione {self.funzione} cromosoma : {self.cromosoma}"

    def __repr__(self):
        return f"{self.id} {self.funzione} {self.cromosoma}"
