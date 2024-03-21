from extensions import db

class EmpresaCnae(db.Model):
    __tablename__ = 'empresa_cnae'
    id = db.Column(db.Integer, primary_key=True)
    cnae_id = db.Column(db.Integer, db.ForeignKey('cnae.id'), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    primario = db.Column(db.Boolean, nullable=False)
    cnae = db.relationship('Cnae', backref='empresa_cnaes')
    empresa = db.relationship('Empresa', backref='empresa_cnaes')
