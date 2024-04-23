from flask import Blueprint, jsonify, request
from services.estabelecimento_service import EstabelecimentoService

estabelecimento_blueprint = Blueprint('estabelecimento', __name__, url_prefix='/estabelecimento')
service = EstabelecimentoService()

@estabelecimento_blueprint.route('/', methods=['GET'])
def get():
  filters = {
    'cnae': request.args.get('cnae'),
    'porte': request.args.get('porte'),
    'razao_social': request.args.get('razao_social'),
    'capital_social_min': request.args.get('capital_social_min', type=float),
    'natju': request.args.get('natju'),
    'logradouro': request.args.get('logradouro'),
    'numero': request.args.get('numero'),
    'cidade': request.args.get('cidade'),
    'situacao': request.args.get('situacao'),
    'matriz' : request.args.get('matriz'),
    'data_abertura': request.args.get('data_abertura'),
    'cnpj': request.args.get('cnpj'),
  }
  filters = {k: v for k, v in filters.items() if v is not None}

  if filters:
      estabelecimentos = service.get_filtered(filters)
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
