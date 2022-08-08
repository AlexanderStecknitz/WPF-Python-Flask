from repository.kunden import kunden
from flask import current_app

class KundeWriteService:
    """
    CustomerWriteService
    """

    def __init__(self):
        pass

    def delete_by_id(self, kunde_id):
        current_app.logger.info('delete kunde with id: %d', kunde_id)
        kunden.remove(kunde_id)