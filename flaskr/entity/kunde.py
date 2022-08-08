"""Entity"""
from dataclasses import dataclass


@dataclass()
class Kunde:
    """
    Entity
    """
    id: int
    nachname: str
    vorname: str
