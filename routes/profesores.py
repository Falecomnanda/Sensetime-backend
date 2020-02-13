from flask import Blueprint, request, jsonify
from models import db, Profesor
from flask_jwt_extended import (jwt_required)

route_profesores = Blueprint('route_profesores', __name__)

@route_profesores.route('/profesores', methods=['GET','POST'])
@route_profesores.route('/profesores/<int:id>', methods=['GET','PUT','DELETE'])
#@jwt_required
def profesores(id=None):
    if request.method == 'GET':
        if id is not None:
            profesor = Profesor.query.get(id)
            if profesor:
                return jsonify(profesor.serialize()), 200
            else:
                return jsonify({"profesor":"not found"}), 404
        else:
            profesores = Profesor.query.all()
            profesores = list(map(lambda profesor: profesor.serialize(), profesores))
            return jsonify(profesores), 200
    
    if request.method == 'POST':

        profesor = Profesor()
        profesor.profesor = request.json.get('profesor')
        profesor.telefono = request.json.get('telefono')
        profesor.rut = request.json.get('rut')
        profesor.email = request.json.get('email')
        
       
        
        db.session.add(profesor)
        db.session.commit()


        return jsonify(profesor.serialize()), 201
    
    if request.method == 'PUT':

        profesor = Profesor.query.get(id)
        profesor.profesor = request.json.get('profesor')
        profesor.telefono = request.json.get('telefono')
        profesor.rut = request.json.get('rut')
        profesor.email = request.json.get('email')
        
        
        
        db.session.commit()

        return jsonify(profesor.serialize()), 200


    if request.method == 'DELETE':
        profesor = Profesor.query.get(id)
        
        
        db.session.delete(profesor)
        db.session.commit()

        return jsonify({'profesor': 'deleted',}), 400

