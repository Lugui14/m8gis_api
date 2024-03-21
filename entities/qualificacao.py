from extensions import db

class Qualificacao(db.Model):
    __tablename__ = 'qualificacao'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
