"""CustomerReadService"""
from flask import current_app
from repository.kunden import kunden


class KundeReadService:
    """
    CusotmerReadService
    """

    def __init__(self):
        pass

    def find(self,
             args: dict,
             ):
        """
        find customer in dependence of query params
        :param args: query params
        :return: customer from the repository or empty list
        """
        current_app.logger.info('find')
        if len(args) == 0:
            return self.find_all()
        for key, value in args.items():
            if key == "nachname":
                return self.find_by_nachname(value)
        return None

    def find_by_nachname(self, nachname):
        """
        find customer by nachname
        :return: mock customer
        """

        found_kunden = []

        for kunde in kunden:
            if kunde.nachname == nachname:
                found_kunden.append(kunde)

        if len(found_kunden) == 0:
            found_kunden = None
        return found_kunden

    def find_by_id(self, id):
        """
        Test
        :return:
        """
        current_app.logger.info('find_by_id')
        for kunde in kunden:
            if kunde.id == id:
                return kunde
        return None

    def find_all(self):
        """
        find all customer
        :return: mock customer
        """
        current_app.logger.info('find_all repository')
        kunde = kunden
        return kunde
