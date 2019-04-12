import secrets
from pyprimes import isprime


bits = 1024
public_exponent = 65537
first = 2 ** (bits - 1)
last = (2 ** bits) - 1


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a, b):
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b


def get_random_number():
    generator = secrets.SystemRandom()
    return generator.randint(first, last)


def get_random_prime():
    while True:
        number = get_random_number()
        if isprime(number):
            return number


def generate_primes():
    primes = []

    while len(primes) < 2:
        number = get_random_prime()
        if number not in primes:
            primes.append(number)
    return primes


def get_keys():
    primes = generate_primes()

    public_modulus = primes[0]*primes[1]
    totient = (primes[0] - 1) * (primes[1] - 1)
    private_exponent = modinv(public_exponent, totient)

    return public_modulus, public_exponent, private_exponent
