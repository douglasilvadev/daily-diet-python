from app import db

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    na_dieta = db.Column(db.Boolean, nullable=False)

db.create_all()  # Criar o banco de dados

# commits e snapshots de dados ficam em routes.py
