from flask import Flask, render_template
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def hello_world():
    saludo = "hola"
    lista = ("fernando", True, 34)
    return render_template("index.html", saludo=saludo, l=lista)
