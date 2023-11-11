import os
import time
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='static')
idSave = 0
info_1 = 'visible'
info_2 = 'hidden'
search_1 = 'hidden'

con = mysql.connector.connect(
    host = os.environ['host'],
    port = os.environ['port'],
    database = os.environ['database'],
    user = os.environ['user'],
    password = os.environ['password']
    )

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/<id>', methods=['GET','POST'])
def infoPokemons(id):
    global idSave
    cursor = con.cursor()
    try:
        id = int(id)
        cursor.execute('SELECT * FROM Pokemon where id = %s', (id,))
    except:
        cursor.execute('SELECT * FROM Pokemon where nome = %s', (id,))
    pokemons = cursor.fetchone()
    cursor.close()
    if not pokemons:
        return 'Unknow'
    id = pokemons[0]
    idSave = id
    return render_template('index.html', id = id, nome = pokemons[1],
                           tipo = pokemons[2], categoria = pokemons[3],
                           habilidade = pokemons[4], peso = pokemons[5],
                           altura = pokemons[6], fraqueza = pokemons[7],
                           descricao = pokemons[8], info_1 = info_1,
                           info_2 = info_2, search_1 = search_1)

@app.route('/increment', methods=['GET','POST'])
def increment():
    global idSave
    idSave += 1
    id = idSave
    return redirect(url_for('infoPokemons', id = id))
@app.route('/decrease', methods=['GET', 'POST'])
def decrease():
    global idSave
    if idSave > 1:
        idSave -= 1
    id = idSave
    return redirect(url_for('infoPokemons', id = id))

@app.route('/passInfo', methods=['POST'])
def passInfo():
    global info_1
    global info_2
    if info_1 == 'visible':
        info_1 = 'hidden'
        info_2 = 'visible'
    else:
        info_1 = 'visible'
        info_2 = 'hidden'
    id = idSave
    return redirect(url_for('infoPokemons', id = id))

@app.route('/search', methods=['POST'])
def search():
    global search_1
    if search_1 == 'visible':
        search_1 = 'hidden'
    else:
        search_1 = 'visible'
    id = idSave
    return redirect(url_for('infoPokemons', id = id))

@app.route('/searchPokemons', methods=['GET', 'POST'])
def searchPokemons():
    searchPokemon = request.form.get('searchPokemon')
    return redirect(url_for('infoPokemons', id = searchPokemon))


app.run(debug=True)

