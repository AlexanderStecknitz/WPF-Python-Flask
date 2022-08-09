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
                return self.find_by_nachname()
        return None

    def find_by_nachname(self):
        """
        find customer by nachname
        :return: mock customer
        """

    def find_all(self):
        """
        find all customer
        :return: mock customer
        """
        current_app.logger.info('find_all repository')
        kunde = kunden
        return kunde