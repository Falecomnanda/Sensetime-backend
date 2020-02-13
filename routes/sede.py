from flask import Blueprint, request, jsonify
from models import db, Sede
from flask_jwt_extended import (jwt_required)

route_sedes = Blueprint('route_sedes', __name__)

@route_sedes.route('/sedes', methods=['GET','POST'])
@route_sedes.route('/sedes/<int:id>', methods=['GET','PUT','DELETE'])
#@jwt_required
def sedes(id=None):
    if request.method == 'GET':
        if id is not None:
            sede = Sede.query.get(id)
            if sede:
                return jsonify(sede.serialize()), 200
            else:
                return jsonify({"sede":"not found"}), 404
        else:
            sedes = Sede.query.all()
            sedes = list(map(lambda sede: sede.serialize(), sedes))
            return jsonify(sedes), 200
    
    if request.method == 'POST':
        sede = Sede()
        sede.sede = request.json.get('sede')
       
        
        db.session.add(sede)
        db.session.commit()


        return jsonify(sede.serialize()), 201
    
    if request.method == 'PUT':
        sede = Sede.query.get(id)
        sede.sede = request.json.get('sede')
        
        
        db.session.commit()

        return jsonify(sede.serialize()), 200


    if request.method == 'DELETE':
        sede = Sede.query.get(id)
        db.session.delete(sede)

        db.session.commit()

        return jsonify({'sede': 'deleted'}), 400




