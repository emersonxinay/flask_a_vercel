from flask import Flask, render_template
app = Flask(__name__,  template_folder='../templates',  static_folder='../static')

@app.route("/")
def inicio():
  return render_template('index.html')

@app.route("/nosotros")
def nosotros():
  return render_template('nosotros.html')

@app.route("/contacto")
def contacto():

  return render_template('contacto.html')

if __name__ == "__main__":
  app.run(debug=True)
  