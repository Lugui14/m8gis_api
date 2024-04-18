from flask import Blueprint, jsonify, request
from services.empresa_service import EmpresaService

empresa_blueprint = Blueprint('empresa', __name__, url_prefix='/empresa')
service = EmpresaService()

@empresa_blueprint.route('/', methods=['GET'])
def get():
  filters = {
    'cnae': request.args.get('cnae'),
    'porte': request.args.get('porte'),
    'razao_social': request.args.get('razao_social'),
    'capital_social_min': request.args.get('capital_social_min', type=float),
    'natureza_juridica': request.args.get('natureza_juridica'),
    # Adicione mais parâmetros de filtro conforme necessário
  }
  filters = {k: v for k, v in filters.items() if v is not None}

  if filters is not None:
    empresas = service.get_filtered(filters)
    return jsonify(empresas)
  else:
    page = request.args.get('page', 1, type=int)
    return jsonify(service.get_all(page))

@empresa_blueprint.route('/<int:id>', methods=['GET'])
def get_by_id(id):
  return jsonify(service.get_by_id(id))

@empresa_blueprint.route('/', methods=['POST'])
def create():
  data = request.json
  return jsonify(service.create(data))

@empresa_blueprint.route('/', methods=['PUT'])
def update():
  data = request.json
  return jsonify(service.update(data))

@empresa_blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id):
  return jsonify(service.delete(id))
