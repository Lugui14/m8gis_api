from extensions import db

class SocioEmpresa(db.Model):
    __tablename__ = 'socio_empresa'
    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    socio_id = db.Column(db.Integer, db.ForeignKey('socio.id'), nullable=False)
    empresa = db.relationship('Empresa', backref='socio_empresas')
    socio = db.relationship('Socio', backref='socio_empresas')
