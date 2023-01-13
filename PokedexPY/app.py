from flask import Flask, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, static_folder='static')

@app.route('/')
@app.route('/index')
def index():
    nome = "Eu"
    dados = {"Prof": "Teac"}
    return render_template('index.html', nome=nome, dados=dados)

con = mysql.connector.connect(
    host='containers-us-west-110.railway.app',
    port='7415',
    database='railway',
    user = 'root',
    password = 'rvDfUENmgLTJlaqXODGf'
    )

@app.route('/info/<id>')
def info(id):
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Pokemon where id = 1')
    result = cursor.fetchall()
    return jsonify(result)



