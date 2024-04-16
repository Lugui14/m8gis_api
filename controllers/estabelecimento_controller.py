from flask import Blueprint, jsonify, request
from services.estabelecimento_service import EstabelecimentoService

estabelecimento_blueprint = Blueprint('estabelecimento', __name__, url_prefix='/estabelecimento')
service = EstabelecimentoService()

@estabelecimento_blueprint.route('/', methods=['GET'])
def get():
  cnpj_id = request.args.get('cnpj', default=None, type=int)
  if cnpj_id is not None:
      estabelecimentos = service.get_by_cnpj(cnpj_id)
      return jsonify(estabelecimentos)
  else:
    page = request.args.get('page', 1, type=int)
    return jsonify(service.get_all(page))

@estabelecimento_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
  return jsonify(service.get_by_id(id))

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
