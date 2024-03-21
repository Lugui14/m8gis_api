from extensions import db

class Cnae(db.Model):
    __tablename__ = 'cnae'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
