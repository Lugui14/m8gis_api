from extensions import db

class NaturezaJuridica(db.Model):
    __tablename__ = 'natureza_juridica'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
