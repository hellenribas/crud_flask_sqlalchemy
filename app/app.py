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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
