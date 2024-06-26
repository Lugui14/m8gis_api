from extensions import db

class Socio(db.Model):
    __tablename__ = 'socio'
    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(15), nullable=True)
    nome_socio = db.Column(db.String(250), nullable=False)
    representante_legal = db.Column(db.String(12))
    nome_representante_legal = db.Column(db.String(250))
    identificador_socio = db.Column(db.String(1), nullable=True)
    data_entrada_sociedade = db.Column(db.Date, nullable=True)
    qualificacao_id = db.Column(db.Integer, db.ForeignKey('qualificacao.id'), nullable=False)
    representante_legal_qualificacao_id = db.Column(db.Integer, db.ForeignKey('qualificacao.id'))
    qualificacao = db.relationship('Qualificacao', foreign_keys=[qualificacao_id], backref='socios')
    representante_qualificacao = db.relationship('Qualificacao', foreign_keys=[representante_legal_qualificacao_id])