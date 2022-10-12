from flask import Flask, make_response, jsonify, request, render_template
import mysql.connector


app = Flask(__name__)

config = {
        'user': 'carford',
        'password': 'carford123',
        'host': '172.22.0.2',
        'port': '3306',
        'database': 'carford_db'
    }

connection = mysql.connector.connect(**config)

@app.route('/proprietarios', methods=['GET'])
def getProp():
    cursor = connection.cursor()
    query = 'SELECT * FROM proprietarios'
    cursor.execute(query)
    proprietarios = cursor.fetchall()
    props = []
    for prop in proprietarios:
      obj = { "id": prop[0], "name": prop[1], "oportunidade_venda": prop[2] }
      props.append(obj)
    return jsonify({ "status": 200, "message": props })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
