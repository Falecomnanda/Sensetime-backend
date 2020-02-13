from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    fullname=db.Column(db.String(50), nullable=False)
    phone=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return 'User %r' % self.username

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'phone': self.phone,
        }

class Profesor(db.Model):
    __tablename__ = 'profesores'
    id=db.Column(db.Integer, primary_key=True)
    profesor=db.Column(db.String(50), nullable=False)
    telefono=db.Column(db.String(50), nullable=False)
    rut=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Profesor %r' % self.profesor

    def serialize(self):
        return{
            'id': self.id,
            'profesor': self.profesor,
            'telefono': self.telefono,
            'rut': self.rut,
            'email': self.email,
            
        }

class Sede(db.Model):
    __tablename__ = 'sedes'
    id=db.Column(db.Integer, primary_key=True)
    sede=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Sede %r' % self.sede

    def serialize(self):
        return{
            'id': self.id,
            'sede': self.sede,
        }

class Curso(db.Model):
    __tablename__ = 'cursos'
    id=db.Column(db.Integer, primary_key=True)
    curso=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Curso %r' % self.curso

    def serialize(self):
        return{
            'id': self.id,
            'curso': self.curso,
        }

class DetailsCurso(db.Model):
    __tablename__ = 'detailscursos'
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.String(50), nullable=False)
    hora=db.Column(db.String(50), nullable=False)
    text=db.Column(db.String(200), nullable=False)
    
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    curso = db.relationship(Curso)
    sede_id = db.Column(db.Integer, db.ForeignKey('sedes.id'), nullable=False)
    sede = db.relationship(Sede)
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesores.id'), nullable=False)
    profesor = db.relationship(Profesor)

    def __repr__(self):
        return 'DetailsCurso %r' % self.curso

    def serialize(self):
        return{
            'id': self.id,
            'curso': self.curso.serialize(),
            'sede': self.sede.serialize(),
            'profesor': self.profesor.serialize(),
            'fecha': self.fecha,
            'hora': self.hora,
            'text': self.text
        }

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id=db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    cliente = db.relationship(User)

    detailscurso_id = db.Column(db.Integer, db.ForeignKey('detailscursos.id'), nullable=False)
    detailscurso = db.relationship(DetailsCurso) #Las relaciones de relationship es sempre para el nombre del modelo

    def __repr__(self):
       return 'Reserva %r' % self.user.username

    def serialize(self):
        user = None
        detailscurso = None
        
        if self.detailscurso_id:
            dc = DetailsCurso.query.get(self.detailscurso_id)
            detailscurso = dc.serialize()
        
        if self.user_id:
            u = User.query.get(self.user_id)
            user = u.serialize()

        return {
            'id': self.id,
            'user_id': self.user_id,
            'detailscurso_id': self.detailscurso_id
        } 
