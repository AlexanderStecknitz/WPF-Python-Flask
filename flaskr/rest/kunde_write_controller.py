"""Test"""
from dependency_injector.wiring import inject, Provide
from flask import Blueprint, jsonify, current_app, request, json, Response
from werkzeug.exceptions import HTTPException

from container import Container
from services.kunde_write_service import KundeWriteService

kunde_write_controller = Blueprint("KundeWriteController", __name__)


@kunde_write_controller.delete('/api/<int:kunde_id>')
@inject
def delete_by_id(kunde_id,
                 write_service: KundeWriteService = Provide[Container.kunde_write_service]):
    """
    Test
    :param kunde_id:
    :param write_service:
    :return:
    """
    current_app.logger.info('delete kunde with id: %s', kunde_id)
    write_service.delete_by_id(kunde_id=kunde_id)
    return jsonify(201)


@kunde_write_controller.post('/api')
@inject
def create_kunde(
        write_service: KundeWriteService = Provide[Container.kunde_write_service]
):
    """
    Test
    :param write_service:
    :return:
    """
    kunde = request.get_json()
    current_app.logger.info(kunde)
    write_service.create_kunde(kunde)
    return Response(status=201, mimetype='application/json')


@kunde_write_controller.put('/api/<int:kunde_id>')
@inject
def update_kunde(
        kunde_id,
        write_service: KundeWriteService = Provide[Container.kunde_write_service]
):
    kunde = request.get_json()
    current_app.logger.info(kunde)
    write_service.update_kunde(kunde=kunde, id=kunde_id)
    return Response(status=204, mimetype='application/json')


@kunde_write_controller.errorhandler(HTTPException)
def handle_exception(e):
    """
    Error Handling
    :param e:
    :return:
    """
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
