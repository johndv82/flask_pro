from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    saludo = "hola"
    lista = ("fernando", True, 34)
    return render_template("index.html", saludo=saludo, l=lista)
