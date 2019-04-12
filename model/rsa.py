from utils.key_generator import get_keys
import logging


class RSA:

    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

    def sign(self, m):
        return self.encrypt(m)

    def verify(self, k):
        return self.decrypt(k)

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, k):
        return pow(k, self.d, self.n)


logging.info('Generating RSA keys...')

n, e, d = get_keys()
rsa = RSA(n, e, d)
