from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
  return "Hola mundo"

@app.route("/nosotros")
def nosotros():
  return "Bienvenido a nosotros"