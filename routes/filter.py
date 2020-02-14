from flask import Blueprint, request, jsonify
from models import db, DetailsCurso, Curso, Sede, Profesor
from flask_jwt_extended import (jwt_required)


route_filters = Blueprint('route_filters', __name__)

@route_filters.route('/filters', methods=['POST'])
#@jwt_required
def filter():

        if request.method == 'POST':
                #validar la informacao
                print(request.get_json())
                sede_id = int(request.json.get('sede_id'))
                profesor_id = int(request.json.get('profesor_id'))
                curso_id = int(request.json.get('curso_id'))

                if sede_id > 0 and profesor_id > 0 and curso_id > 0:
                        details_cursos = DetailsCurso.query.filter_by(curso_id = curso_id, sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200
                elif sede_id > 0 and profesor_id == 0 and curso_id == 0:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200

                elif sede_id > 0 and profesor_id > 0 and curso_id == 0:
                        details_cursos = DetailsCurso.query.filter_by(sede_id = sede_id, profesor_id = profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id == 0 and profesor_id == 0 and curso_id > 0:
                        details_cursos = DetailsCurso.query.filter_by(curso_id = curso_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id == 0 and profesor_id > 0 and curso_id == 0:
                        details_cursos = DetailsCurso.query.filter_by(profesor_id=profesor_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                elif sede_id > 0 and profesor_id == 0 and curso_id > 0:
                        details_cursos = DetailsCurso.query.filter_by(curso_id = curso_id, sede_id = sede_id).all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200 

                else:
                        details_cursos = DetailsCurso.query.all()
                        details_cursos = list(map(lambda details_curso: details_curso.serialize(), details_cursos))
                        
                        return jsonify(details_cursos), 200         
                
                


        