import secrets
from mod import Mod
from pyprimes import isprime


def generate_primes(bits):
    generator = secrets.SystemRandom()
    primes = []
    number = generator.randint(2**bits, 2**(bits+1)-1)
    while len(primes) < 2:
        if isprime(number) and number not in primes:
            primes.append(number)
        number = generator.randint(2 ** bits, 2 ** (bits + 1) - 1)
    return primes
