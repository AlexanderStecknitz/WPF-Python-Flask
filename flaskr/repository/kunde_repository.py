from flask import current_app
from .kunden import kunden

class KundeRepository:
    def find_all(self):
        current_app.logger.info('find_all repository')
        kunde = kunden
        return kunde