
from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Run App Cristian Tertuliano"

if __name__ == '__main__':
    app.run()