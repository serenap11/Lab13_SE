from dataclasses import dataclass

from model.gene import Gene


@dataclass
class Interazione:
    g1 : Gene
    g2 : Gene
    tipo : str
    correlazione : float

    def __str__(self):
        return f"{self.g1} - {self.g2} tipo : {self.tipo} correlazione : {self.correlazione}"

    def __repr__(self):
        return f"{self.g1} {self.g2} {self.tipo} {self.correlazione}"