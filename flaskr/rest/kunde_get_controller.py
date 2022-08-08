"""CustomerGetController"""

from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
from services.kunde_read_service import KundeReadService
from container import Container

kunde_getcontroller = Blueprint('KundeGetController', __name__)


"""
    find with query parameter
    :param read_service: ReadService with Dependency Injection
    :return: JSON of customer
"""
@kunde_getcontroller.get('/api')
@inject
def find(
        read_service: KundeReadService = Provide[Container.kunde_read_service]
):
    args = request.args
    current_app.logger.info('find %s', args.to_dict())
    kunden = read_service.find(args)
    return jsonify(kunden)
