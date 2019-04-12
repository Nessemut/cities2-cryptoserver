from flask import Blueprint, request
from model.rsa import rsa
import math
from json import dumps

rsa_blueprint = Blueprint('rsa', __name__, url_prefix='/rsa')


@rsa_blueprint.route('/sign', methods=['POST'])
def sign():
    message = request.form['message']
    m = int.from_bytes(message.encode(), 'big')
    s = rsa.sign(m)
    return str(s)


@rsa_blueprint.route('/verify', methods=['POST'])
def verify():
    k = int(request.form['message'])
    v = rsa.verify(k)
    n = math.ceil(v.bit_length() / 8)
    m = str((v.to_bytes(n, 'big')).decode())

    return m


@rsa_blueprint.route('/getpubkey')
def get_kpub():
    res = {}
    res.update({'e': rsa.e})
    res.update({'n': rsa.n})
    return dumps(res)
