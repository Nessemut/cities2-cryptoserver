from flask import Flask
from api.rsa_blueprint import rsa_blueprint


app = Flask(__name__)

app.register_blueprint(rsa_blueprint)

if __name__ == '__main__':
    app.run(port=5500)
