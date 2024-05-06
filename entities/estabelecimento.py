from extensions import db

class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimento'
    id = db.Column(db.Integer, primary_key=True)
    cnpj_basico = db.Column(db.String(8), nullable=False)
    cnpj_ordem = db.Column(db.String(4), nullable=False)
    cnpj_dv = db.Column(db.String(2), nullable=False)
    identificador_matriz_filial = db.Column(db.Integer, nullable=False)
    nome_fantasia = db.Column(db.String(100), nullable=True)
    situacao_cadastral = db.Column(db.Integer, nullable=False)
    data_inicio_atividade = db.Column(db.Date, nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=True)
    empresa = db.relationship('Empresa', backref='estabelecimentos')
    endereco = db.relationship('Endereco', backref='estabelecimentos')