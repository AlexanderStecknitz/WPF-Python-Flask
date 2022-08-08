from flask import Blueprint, jsonify, current_app, request
from dependency_injector.wiring import inject, Provide
from container import Container
from services.kunde_write_service import KundeWriteService

kunde_write_controller = Blueprint("KundeWriteController", __name__)


@kunde_write_controller.delete('/api/<int:kunde_id>')
@inject
def delete_by_id(kunde_id,
                 write_service: KundeWriteService = Provide[Container.kunde_write_service]):
    current_app.logger.info('delete kunde with id: %s', kunde_id)
    write_service.delete_by_id(kunde_id=kunde_id)
    return jsonify(201)
