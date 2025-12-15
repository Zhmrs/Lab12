from dataclasses import dataclass
import datetime
from model.rifugio import Rifugio


@ dataclass
class Connessione:
    id:int
    id_rifugio1:Rifugio
    id_rifugio2:Rifugio
    distanza : float
    difficolta:str
    durata: datetime.time
    anno:int

    def calcola_peso(self):
        fattori = {"facile": 1, "media": 1.5, "difficile": 2}
        return self.distanza * fattori[self.difficolta]