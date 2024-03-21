from extensions import db

class Empresa(db.Model):
    __tablename__ = 'empresa'
    id = db.Column(db.Integer, primary_key=True)
    cnpj_basico = db.Column(db.String(8), nullable=False)
    porte = db.Column(db.Integer, nullable=False)
    razao_social = db.Column(db.String(100), nullable=False)
    natureza_juridica_id = db.Column(db.Integer, db.ForeignKey('natureza_juridica.id'), nullable=False)
    natureza_juridica = db.relationship('NaturezaJuridica', backref='empresas')
