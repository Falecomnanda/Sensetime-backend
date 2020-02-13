from flask import Blueprint, request, jsonify
from models import db, DetailsCurso, Curso, Sede, Profesor
from flask_jwt_extended import (jwt_required)


route_filters = Blueprint('route_filters', __name__)

@route_filters.route('/filters', methods=['GET','POST'])
@route_filters.route('/filters/<int:id>', methods=['GET','PUT','DELETE'])
#@jwt_required

def filter (id=None):

        if request.method == 'POST':
                #validar la informacao
                sede_id = request.json.get('sede_id', None)
                profesor_id = request.json.get('profesor_id', None)
                curso_id = request.json.get('curso_id', None)

                if sede_id is not None and profesor_id is not None and curso_id is not None:
                        details_cursos = DetailsCurso.query.filter_by(curso_id = curso_id, sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id is not None and profesor_id is not None and curso_id is None:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id is not None and profesor_id is None and curso_id is None:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200

                elif sede_id is None and profesor_id is None and curso_id is None:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id is None and profesor_id is None and curso_id is not None:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id is None and profesor_id is None and curso_id is None:
                        details_cursos = DetailsCurso.query.all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200         
                
                


        