from flask import Flask, render_template, request
import datetime
app = Flask(__name__,  template_folder='../templates',  static_folder='../static')

@app.route("/")
def inicio():
  year_actual = datetime.datetime.now().year
  return render_template('cachipun.html', year_actual=year_actual)

@app.route("/nosotros")
def nosotros():
  return render_template('nosotros.html')

@app.route("/contacto")
def contacto():

  return render_template('contacto.html')

# juego cachipun
@app.route('/cachipun')
def cachipun():
    return render_template('cachipun.html', resultado='')

@app.route('/jugar', methods=['POST'])
def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    opcion_usuario = request.form['opcion']
    import random
    opcion_maquina = random.choice(opciones)

    if opcion_usuario == opcion_maquina:
        resultado = '¡Empate!'
    elif (
        (opcion_usuario == 'piedra' and opcion_maquina == 'tijeras') or
        (opcion_usuario == 'papel' and opcion_maquina == 'piedra') or
        (opcion_usuario == 'tijeras' and opcion_maquina == 'papel')
    ):
        resultado = '¡Ganaste!'
    else:
        resultado = '¡Perdiste!'

    return render_template('cachipun.html', resultado=f'{resultado}', opcion_usuario = f'{opcion_usuario}', opcion_maquina = f'{opcion_maquina}')


if __name__ == "__main__":
  app.run(debug=True)
  