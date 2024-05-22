from extensions import db

class MotivoSituacao(db.Model):
    __tablename__ = 'motivo_situacao'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
