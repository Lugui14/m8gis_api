from extensions import db

class Endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False, default='')
    logradouro = db.Column(db.String(150), nullable=False, default='')
    cep = db.Column(db.BigInteger, nullable=False)
    bairro = db.Column(db.String(50), nullable=True, default='')
    tipo_logradouro = db.Column(db.String(50), nullable=False, default='')
    complemento = db.Column(db.String(160), nullable=False, default='')
    latitude = db.Column(db.Numeric, nullable=True)
    longitude = db.Column(db.Numeric, nullable=True)
    __table_args__ = (db.UniqueConstraint('logradouro', 'numero', 'bairro', 'tipo_logradouro', 'cep', 'municipio_id', 'complemento'),)
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id'), nullable=False)

class Municipio(db.Model):
    __tablename__ = 'municipio'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    uf_id = db.Column(db.Integer, db.ForeignKey('uf.id'), nullable=False)
    uf = db.relationship('Uf', back_populates="municipios")
    enderecos = db.relationship('Endereco', backref='municipio', lazy=True)

class Uf(db.Model):
    __tablename__ = 'uf'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    qtd_estabelecimentos = db.Column(db.Integer, nullable=True)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

Uf.municipios = db.relationship('Municipio', order_by=Municipio.id, back_populates="uf")

class Pais(db.Model):
    __tablename__ = 'pais'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    ufs = db.relationship('Uf', backref='pais', lazy=True, cascade="all, delete")