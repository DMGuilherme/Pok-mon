import json

from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__, static_folder='static')

con = mysql.connector.connect(
    host='containers-us-west-110.railway.app',
    port='7415',
    database='railway',
    user = 'root',
    password = 'rvDfUENmgLTJlaqXODGf'
    )
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<id>')
def infoPokemons(id):
    #id = int(request.form['id'])
    #action = request.form['changePokemon']
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Pokemon where id = {}'.format(id))
    #if action == 'increment':

    #elif action == 'decrement':
        #cursor.execute('SELECT * FROM Pokemon where id = {}'.format(id))

    result = cursor.fetchall()
    pokemons = json.loads(jsonify(result).get_data())
    [(id_, nome_, tipo_, categoria_, habilidade_, peso_, altura_, fraqueza_, descricao_)] = pokemons
    nome = nome_
    tipo = tipo_
    categoria = categoria_
    habilidade = habilidade_
    peso = peso_
    altura = altura_
    fraqueza = fraqueza_
    descricao = descricao_
    return render_template('index.html', nome = nome,
                           tipo = tipo, categoria = categoria,
                           habilidade = habilidade, peso = peso,
                           altura = altura, fraqueza = fraqueza,
                           descricao = descricao)

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


