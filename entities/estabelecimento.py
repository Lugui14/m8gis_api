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
    data_situacao_cadastral = db.Column(db.Date, nullable=True)
    motivo_situacao_cadastral_id = db.Column(db.Integer, db.ForeignKey('motivo_situacao.id'), nullable=False)
    ddd = db.Column(db.String(4), nullable=True)
    telefone = db.Column(db.String(9), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=True)
    empresa = db.relationship('Empresa', backref='estabelecimentos')
    endereco = db.relationship('Endereco', backref='estabelecimentos')
    motivo_situacao = db.relationship('MotivoSituacao', backref='estabelecimentos')
    __table_args__ = (db.UniqueConstraint('cnpj_basico', 'cnpj_ordem', 'cnpj_dv'),)

