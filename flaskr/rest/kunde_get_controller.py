"""CustomerGetController"""

from flask import Blueprint, jsonify, current_app, request, abort, json
from dependency_injector.wiring import inject, Provide
from services.kunde_read_service import KundeReadService
from container import Container
from werkzeug.exceptions import HTTPException

kunde_get_controller = Blueprint('KundeGetController', __name__)

"""
    find with query parameter
    :param read_service: ReadService with Dependency Injection
    :return: JSON of customer
"""


@kunde_get_controller.get('/api')
@inject
def find(
        read_service: KundeReadService = Provide[Container.kunde_read_service]
):
    args = request.args
    current_app.logger.info('find %s', args.to_dict())
    kunden = read_service.find(args=args)
    if kunden is None:
        return jsonify(abort(404))
    return jsonify(kunden)


@kunde_get_controller.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
