from flask import Blueprint, jsonify, request
from services.estabelecimento_service import EstabelecimentoService

estabelecimento_blueprint = Blueprint('estabelecimento', __name__, url_prefix='/estabelecimento')
service=EstabelecimentoService()
@estabelecimento_blueprint.route('/estabelecimentos', methods=['POST'])
def get_estabelecimentos():
    filters = request.get_json()

    print(filters)

    if filters:
        estabelecimentos = service.get_filtered(filters)
        return jsonify(estabelecimentos)
    else:
        page = request.args.get('page', 0, type=int)
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
