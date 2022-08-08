"""Test"""
from flask import current_app
from repository.kunde_repository import KundeRepository


class KundeReadService:
    """
    Test
    """

    def __init__(self):
        pass

    def find(self,
             args: dict):
        if len(args) == 0:
            return KundeRepository.find_all(self)


