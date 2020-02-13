from flask import Blueprint, request, jsonify
from models import db, DetailsCurso, Curso, Sede, Profesor
from flask_jwt_extended import (jwt_required)

route_detailscursos = Blueprint('route_detailscursos', __name__)

@route_detailscursos.route('/detailscursos', methods=['GET','POST'])
@route_detailscursos.route('/detailscursos/<int:id>', methods=['GET','PUT','DELETE'])
#@jwt_required
def detailscursos(id=None):
    if request.method == 'GET':
        if id is not None:
            detailscursos = DetailsCurso.query.get(id)
            
            if detailscursos:
                return jsonify(detailscursos.serialize()), 200
            else:
                return jsonify({"detailscursos":"not found"}), 404
        else:
            detailscursos = DetailsCurso.query.all()
            detailscursos = list(map(lambda detailscurso: detailscurso.serialize(), detailscursos))
            return jsonify(detailscursos), 200
    
    if request.method == 'POST':
        
        curso_id = request.json.get('curso_id', None)
        if not curso_id:
            return jsonify({"msg": "curso is required"}), 422
        else:
            curso = Curso.query.get(curso_id)
            if not curso:
                return jsonify({"msg": "curso doesn't exist"}), 422
            

        sede_id = request.json.get('sede_id', None)
        if not sede_id:
            return jsonify({"msg": "sede is required"}), 422
        else:
            sede = Sede.query.get(sede_id)
            if not sede:
                return jsonify({"msg": "sede doesn't exist"}), 422


        profesor_id = request.json.get('profesor_id', None)
        if not profesor_id:
            return jsonify({"msg": "profesor is required"}), 422
        else:
            profesor = Profesor.query.get(profesor_id)
            if not profesor:
                return jsonify({"msg": "profesor doesn't exist"}), 422


        
        detailscurso = DetailsCurso()
        detailscurso.curso_id = curso_id
        detailscurso.sede_id = sede_id
        detailscurso.profesor_id = request.json.get('profesor_id', None)
        detailscurso.text = request.json.get('text', None)
        detailscurso.fecha = request.json.get('fecha', None)
        detailscurso.hora = request.json.get('hora', None)


       
        
        db.session.add(detailscurso)
        db.session.commit()


        return jsonify(detailscurso.serialize()), 201
    
    if request.method == 'PUT':
        detailscurso = DetailsCurso.query.get(id)
        detailscurso.curso_id = request.json.get('curso_id')
        detailscurso.sede_id = request.json.get('sede_id')
        detailscurso.profesor_id = request.json.get('profesor_id')
        detailscurso.text = request.json.get('text')
        detailscurso.fecha = request.json.get('fecha')
        detailscurso.hora = request.json.get('hora')
       
        db.session.commit()

        return jsonify(detailscurso.serialize()), 200


    if request.method == 'DELETE':
        detailscurso = DetailsCurso.query.get(id)
        db.session.delete(detailscurso)

        db.session.commit()

        return jsonify({'detailscurso': 'deleted'}), 400

