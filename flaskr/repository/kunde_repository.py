"""Customer Repository"""
from flask import current_app
from .kunden import kunden


class KundeRepository:
    """
    Customer Repositorys with mock functions
    """

    def find_all(self):
        """
        find all customer
        :return: mock customer
        """
        current_app.logger.info('find_all repository')
        kunde = kunden
        return kunde

    def find_by_nachname(self):
        """
        find customer by nachname
        :return: mock customer
        """
