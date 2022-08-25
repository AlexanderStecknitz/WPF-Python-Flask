"""KundeDTO"""
import random
from dataclasses import dataclass
from entity.kunde import Kunde

@dataclass()
class KundeDTO:
    """KundeDTO"""
    vorname: str
    nachname: str

    def to_kunde(self):
        return Kunde(id=random.randint(0,1000),vorname=self.vorname, nachname=self.nachname)