import json

from flask import Flask, render_template, jsonify, redirect, url_for
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
@app.route('/<id>', methods=['GET','POST'])
def infoPokemons(id):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Pokemon where id = {}'.format(id))
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

id = 0
@app.route('/increment', methods=['GET','POST'])
def increment():
    global id
    id += 1
    return redirect(url_for('infoPokemons', id=id))
@app.route('/decrease', methods=['GET', 'POST'])
def decrease():
    global id
    id -= 1
    return redirect(url_for('infoPokemons', id=id))

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


