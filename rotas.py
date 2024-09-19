from flask import request, jsonify
from app import app, db
from modelos import Refeicao
from datetime import datetime

# Registra uma refeição
@app.route('/meals', methods=['POST'])
def add_meals():
    data = request.get_json()
    meal = Refeicao(
        nome=data['nome'],
        descricao=data.get('descricao'),
        data_hora=datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S'),
        na_dieta=data['na_dieta']
    )
    db.session.add(meal)
    db.session.commit()
    return jsonify({'message': 'Refeição adicionada com sucesso!'}), 201

# Lista todas as refeições
@app.route('/meals', methods=['GET'])
def get_meals():
    meals = Refeicao.query.all()
    return jsonify([{
        'id': meal.id,
        'nome': meal.nome,
        'descricao': meal.descricao,
        'data_hora': meal.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
        'na_dieta': meal.na_dieta
    } for meal in meals]), 200

# Visualiza uma refeição específica por ID
@app.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    meal = Refeicao.query.get(id)
    return jsonify({
        'id': meal.id,
        'nome': meal.nome,
        'descricao': meal.descricao,
        'data_hora': meal.data_hora.strftime('%Y-%m-%d %H:%M:%S'),
        'na_dieta': meal.na_dieta
    }), 200

# Edita uma refeição e seus atributos
@app.route('/meals/<int:id>', methods=['PUT'])
def update_meal(id):
    meal = Refeicao.query.get(id)
    data = request.get_json()
    meal.nome = data['nome']
    meal.descricao = data.get('descricao')
    meal.data_hora = datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S')
    meal.na_dieta = data['na_dieta']
    db.session.commit()
    return jsonify({'message': 'Refeição atualizada com sucesso!'}), 200

# Apaga uma refeição da lista
@app.route('/meals/<int:id>', methods=['DELETE'])
def delete_meal(id):
    meal = Refeicao.query.get(id)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'message': 'Refeição deletada com sucesso!'}), 200
