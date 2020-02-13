from flask import Blueprint, request, jsonify
from models import db, Curso
from flask_jwt_extended import (jwt_required)

route_cursos = Blueprint('route_cursos', __name__)

@route_cursos.route('/cursos', methods=['GET','POST'])
@route_cursos.route('/cursos/<int:id>', methods=['GET','PUT','DELETE'])#
#jwt_required
def cursos(id=None):
    if request.method == 'GET':
        if id is not None:
            curso = Curso.query.get(id)
            if curso:
                return jsonify(curso.serialize()), 200
            else:
                return jsonify({"curso":"not found"}), 404
        else:
            cursos = Curso.query.all()
            cursos = list(map(lambda curso: curso.serialize(), cursos))
            return jsonify(cursos), 200
    
    if request.method == 'POST':
        curso = Curso()
        curso.curso = request.json.get('curso')
       
        
        db.session.add(curso)
        db.session.commit()


        return jsonify(curso.serialize()), 201
    
    if request.method == 'PUT':
        curso = Curso.query.get(id)
        curso.curso = request.json.get('curso')
        
        
        db.session.commit()

        return jsonify(curso.serialize()), 200


    if request.method == 'DELETE':
        curso = Curso.query.get(id)
        db.session.delete(curso)

        db.session.commit()

        return jsonify({'curso': 'deleted'}), 400

