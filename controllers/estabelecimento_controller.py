from flask import Blueprint, jsonify, request
from services.estabelecimento_service import EstabelecimentoService

estabelecimento_blueprint = Blueprint('estabelecimento', __name__, url_prefix='/estabelecimento')
service=EstabelecimentoService()
# exemplo de query: http://localhost:8000/estabelecimento/estabelecimentos?porte=3&situacao=2
@estabelecimento_blueprint.route('/estabelecimentos', methods=['GET'])
def get_estabelecimentos():
    filters = {k: request.args.get(k) for k in
               ['id',
                'cnae',
                'cnae_id', 
                'porte', 
                'razao_social',
                'capital_social_min', 
                'natju',
                'logradouro',
                'numero',
                'cidade',
                'situacao',
                'matriz',
                'data_abertura',
                'cnpj']}
    filters = {k: v for k, v in filters.items() if v is not None}

    if filters:
        estabelecimentos = service.get_filtered(filters)
        return jsonify(estabelecimentos)
    else:
        page = request.args.get('page', 1, type=int)
        return jsonify(service.get_all(page))

@estabelecimento_blueprint.route('/<int:id>', methods=['GET'])
def get_estab_details(id):
    estabelecimento_data = service.get_estab_by_id_with_empresa(id)
    
    if estabelecimento_data:
        return jsonify(estabelecimento_data), 200
    else:
        return jsonify({'message': 'Estabelecimento não encontrado'}), 404



@estabelecimento_blueprint.route('/', methods=['POST'])
def create():
  data = request.json
  return jsonify(service.create(data))

@estabelecimento_blueprint.route('/', methods=['PUT'])
def update():
  data = request.json
  return jsonify(service.update(data))

@estabelecimento_blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id):
  return jsonify(service.delete(id))