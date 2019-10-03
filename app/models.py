from app import app, db

class Guia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True, unique=True)
    nivel = db.Column(db.String(120), index=True, unique=True)
    criterios = db.relationship('Criterio', backref='criterio', lazy='dynamic')

    def __repr__(self):
        return '<Guia {} {}>'.format(self.nombre, self.nivel)



class Criterio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(140))
    elementos_control = db.Column(db.String(140))
    guia = db.Column(db.Integer, db.ForeignKey('guia.id'))

    def __repr__(self):
        return '<Criterio {} {} {}>'.format(self.descripcion, self.elementos_control, self.guia)
