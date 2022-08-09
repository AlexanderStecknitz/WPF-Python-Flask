from flask import Blueprint, jsonify, current_app, json
from dependency_injector.wiring import inject, Provide
from container import Container
from services.kunde_write_service import KundeWriteService
from werkzeug.exceptions import HTTPException

kunde_write_controller = Blueprint("KundeWriteController", __name__)


@kunde_write_controller.delete('/api/<int:kunde_id>')
@inject
def delete_by_id(kunde_id,
                 write_service: KundeWriteService = Provide[Container.kunde_write_service]):
    current_app.logger.info('delete kunde with id: %s', kunde_id)
    write_service.delete_by_id(kunde_id=kunde_id)
    return jsonify(201)

@kunde_write_controller.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response