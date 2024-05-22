from extensions import db

class Empresa(db.Model):
    __tablename__ = 'empresa'
    id = db.Column(db.Integer, primary_key=True)
    cnpj_basico = db.Column(db.String(8), nullable=False, unique=True)
    porte = db.Column(db.Integer, nullable=False)
    razao_social = db.Column(db.String(250), nullable=False)
    capital_social = db.Column(db.Numeric, nullable=False)
    natureza_juridica_id = db.Column(db.Integer, db.ForeignKey('natureza_juridica.id'), nullable=False)
    cnae_principal_id = db.Column(db.Integer, db.ForeignKey('cnae.id'), nullable=False)
    natureza_juridica = db.relationship('NaturezaJuridica', backref='empresas')
    cnae = db.relationship('Cnae', backref='empresas')
