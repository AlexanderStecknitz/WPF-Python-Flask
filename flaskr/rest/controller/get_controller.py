from flask import Blueprint

kunde_getcontroller = Blueprint('KundeGetController', __name__)
@kunde_getcontroller.get('/test')
def test():
    return 'Test'
