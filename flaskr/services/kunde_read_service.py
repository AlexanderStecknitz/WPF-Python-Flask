"""CustomerReadService"""
from flask import current_app
from repository.kunde_repository import KundeRepository


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
            return KundeRepository.find_all(self)
        for key, value in args.items():
            if key == "nachname":
                return KundeRepository.find_by_nachname(self)
        empty_list = []
        return empty_list
