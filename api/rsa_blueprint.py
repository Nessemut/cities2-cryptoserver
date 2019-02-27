from flask import Blueprint

from util.primes import generate_primes

rsa_blueprint = Blueprint('rsa', __name__, url_prefix='/rsa')
bits = 1024


@rsa_blueprint.route('/getprimes')
def root():
    return str(generate_primes(bits))
