from flask import Blueprint, request, jsonify
from models import db, Reserva
from flask_jwt_extended import (jwt_required)

route_reservas = Blueprint('route_reservas', __name__)

@route_reservas.route('/reservas', methods=['GET','POST'])
@route_reservas.route('/reservas/<int:id>', methods=['GET','PUT','DELETE'])
#@jwt_required
def reservas (id=None):

    if request.method == 'GET':
        if id is not None:
            reserva = Reserva.query.get(id)
            if reserva:
                return jsonify(reserva.serialize()), 200
            else:
                return jsonify({"reserva":"not found"}), 404
        else:
            reservas = Reserva.query.all()
            reservas= list(map(lambda reser: reser.serialize(), reservas))
            return jsonify(reservas), 200
    
    if request.method == 'POST':
        reserva= Reserva() #Este chama la classe para abaixo inserir o que está dentro da classe
        reserva.detailscurso_id = request.json.get('detailscurso_id')
        reserva.user_id = request.json.get('user_id')
        
        db.session.add(reserva) #este adiciona los datos da tabla
        db.session.commit() #este guarda


        return jsonify(reserva.serialize()), 201 #retorna  un objeto jason dentro de insomnia

    if request.method == 'DELETE':
        reserva = Reserva.query.get(id)
        db.session.delete(reserva)

        db.session.commit()

        return jsonify({'reserva': 'deleted'}), 400