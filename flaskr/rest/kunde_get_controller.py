"""Test"""

from flask import Blueprint, jsonify, current_app
from dependency_injector.wiring import inject, Provide
from services.kunde_read_service import KundeReadService
from container import Container

kunde_getcontroller = Blueprint('KundeGetController', __name__)


@kunde_getcontroller.get('/api')
@inject
def find_all(
        read_service: KundeReadService = Provide[Container.kunde_read_service]
):
    """
    Test
    """
    current_app.logger.info('find_all kunden')
    kunde = read_service.find_all()
    current_app.logger.info('find all kunden: {}', kunde)
    return jsonify(kunde)
