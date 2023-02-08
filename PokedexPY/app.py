import json

from flask import Flask, render_template, jsonify, redirect, url_for, request
import mysql.connector

app = Flask(__name__, static_folder='static')
idSave = 0
info_1 = 'visible'
info_2 = 'hidden'
search_1 = 'hidden'

con = mysql.connector.connect(
    host='containers-us-west-110.railway.app',
    port='7415',
    database='railway',
    user = 'root',
    password = 'XllljYq946VUKVI7Caxl'
    )
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<id>', methods=['GET','POST'])
def infoPokemons(id):
    global idSave
    cursor = con.cursor()
    try:
        id = int(id)
        cursor.execute('SELECT * FROM Pokemon where id = {}'.format(id))
    except:
        cursor.execute('SELECT * FROM Pokemon where nome = "{}"'.format(id))
    result = cursor.fetchall()
    pokemons = json.loads(jsonify(result).get_data())
    if not pokemons:
        return 'Unknow'
    pokemon = pokemons[0]
    id = pokemon[0]
    idSave = id
    return render_template('index.html', id = id, nome = pokemon[1],
                           tipo = pokemon[2], categoria = pokemon[3],
                           habilidade = pokemon[4], peso = pokemon[5],
                           altura = pokemon[6], fraqueza = pokemon[7],
                           descricao = pokemon[8], info_1 = info_1,
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
#[[1,"Bulbasaur","Grass,Poison","Seed","Overgrow",6.9,0.7,"Fire,Psychic,Flying,Ice",""]]

# id
# nome
# tipo
# categoria
# habilidade
# peso
# altura
# fraqueza
# descricao