from repository.kunden import kunden
from rest.kunde_dto import KundeDTO
from flask import current_app

class KundeWriteService:
    """
    CustomerWriteService
    """

    def __init__(self):
        pass

    def delete_by_id(self, kunde_id):
        current_app.logger.info('delete kunde with id: %d', kunde_id)
        for i in kunden:
            if i.id == kunde_id:
                kunden.remove(i)
        current_app.logger.info(kunden)

    def create_kunde(self, kunde):
        current_app.logger.info('create kunde with name: %s and vorname: %s', kunde['nachname'], kunde['vorname'])
        kunde_dto = KundeDTO(vorname=kunde['vorname'], nachname=kunde['nachname'])
        kunde_with_id = kunde_dto.to_kunde()
        kunden.append(kunde_with_id)
        current_app.logger.info(kunden)