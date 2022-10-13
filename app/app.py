from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://carford:carford123@192.168.0.109/carford_db'


connection = SQLAlchemy(app)

class Proprietarios(connection.Model):
  id = connection.Column("id", connection.Integer, primary_key=True)
  nome = connection.Column("nome", connection.String(45))
  oportunidade_venda = connection.Column("oportunidade_venda", connection.Boolean)

  def __init__(self, nome, oportunidade_venda):
    self.nome = nome
    self.oportunidade_venda = oportunidade_venda
  
  def to_json(self):
    return { "id": self.id, "nome": f"{self.nome}", "oportunidade_venda": self.oportunidade_venda }

class Carros(connection.Model):
  id = connection.Column('id', connection.Integer, primary_key=True)
  modelo = connection.Column('modelo', connection.String(45))
  cor = connection.Column('cor', connection.String(45))
  proprietario_id = connection.Column('proprietario_id', connection.Integer)

  def __init__(self, modelo, cor, proprietario_id):
    self.modelo = modelo
    self.cor = cor
    self.proprietario_id = proprietario_id
  
  def to_json(self):
    return { "id": self.id, "modelo": self.modelo, "cor": self.cor, "proprietario_id": self.proprietario_id }


@app.route("/proprietarios", methods=['GET'])
def getProp():
  try:
    proprietarios = Proprietarios.query.all()
    json_convert = [ prop.to_json() for prop in proprietarios ]
    return Response(json.dumps(json_convert), status=200)
  except Exception as ex:
    return Response(json.dumps({ "status": 404, "message": ex.args }), status=404)

@app.route("/carros", methods=['GET'])
def getCar():
  try:
    cars = Carros.query.all()
    json_convert = [ car.to_json() for car in cars ]
    return Response(json.dumps(json_convert), status=200)
  except Exception as ex:
    return Response(json.dumps({ "status": 404, "message": ex.args }), status=404)

@app.route("/proprietario/<id>")
def getPropId(id):
  try:
      proprietario = Proprietarios.query.filter_by(id=id).first()
      json_convert = proprietario.to_json()
      return Response(json.dumps(json_convert), status=200)
  except Exception as ex:
      return Response(json.dumps({ "status": 404, "message": ex.args }), status=404)

@app.route("/carro/<id>")
def getCarId(id):
  try:
      carro = Carros.query.filter_by(id=id).first()
      json_convert = carro.to_json()
      return Response(json.dumps(json_convert), status=200)
  except Exception as ex:
      return Response(json.dumps({ "status": 404, "message": ex.args }), status=404)  

@app.route("/cadastro", methods=['POST'])
def createProp():
  body = request.get_json()

  try:
    proprietario = Proprietarios(nome=body["nome"], oportunidade_venda=body["oportunidade_venda"])
    connection.session.add(proprietario)
    connection.session.commit()
    return Response(json.dumps(proprietario.to_json()))
  except Exception as ex:
    return Response(json.dumps({ "status": 404, "message": ex.args }), status=404) 

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
