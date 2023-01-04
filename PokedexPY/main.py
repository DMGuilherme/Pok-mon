import mysql.connector
from mysql.connector import Error

id = " '3' "
nome = " 'Venusaur' "
tipo = " 'Grass,Poison' "
categoria = " 'Seed' "
habilidade = " 'Overgrow' "
peso = " '100.0' "
altura = " '2.0' "
fraqueza = " 'Fire,Psychic,Flying,Ice' "
descricao = " '' "
var = "(" + id + "," + nome + "," + tipo + "," + categoria + "," + habilidade + "," + peso + "," + altura + "," + fraqueza + "," + descricao + ")"

try:
    con = mysql.connector.connect(host='containers-us-west-110.railway.app', port='7415', database='railway', user = 'root', password = 'rvDfUENmgLTJlaqXODGf')

    inserir_pokemons = """INSERT INTO Pokemon
                        (id, nome, tipo, categoria, habilidade, peso, altura, fraqueza, descricao)
                        VALUES
                        """ + var

    cursor = con.cursor()
    cursor.execute(inserir_pokemons)
    con.commit()
    print(cursor.rowcount, "registro insterido na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir: {}".format(erro))

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("conexão finalizada.")