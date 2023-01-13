from flask import Flask, render_template, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

con = mysql.connector.connect(
    host='containers-us-west-110.railway.app',
    port='7415',
    database='railway',
    user = 'root',
    password = 'rvDfUENmgLTJlaqXODGf'
    )

@app.route('/info')
def info():
    cursor = con.cursor()
    cursor.execute('SELECT * FROM Pokemon where id = 1')
    result = cursor.fetchall()
    return jsonify(result)

