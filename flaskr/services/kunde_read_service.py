"""Test"""

from flask import current_app
from repository.kunde_repository import KundeRepository


class KundeReadService:
    """
    Test
    """

    def __init__(self):
        pass

    def find_all(self):
        """
        Test
        :return:
        """
        current_app.logger.info("KundeReadService find_all")
        return KundeRepository.find_all(self)
