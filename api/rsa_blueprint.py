from flask import Blueprint
from model.rsa import get_keys

rsa_blueprint = Blueprint('rsa', __name__, url_prefix='/rsa')


@rsa_blueprint.route('/getkeys')
def root():
    keys = get_keys()
    return "Kpub: [{}, {}]\nKpriv: [{}, {}]".format(keys[1], keys[0], keys[2], keys[0])
