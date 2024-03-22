from flask import Blueprint, jsonify, request
from services.empresa_service import EmpresaService

empresa_blueprint = Blueprint('empresa', __name__, url_prefix='/empresa')
service = EmpresaService()

@empresa_blueprint.route('/', methods=['GET'])
def get():
  page = request.args.get('page', 1)
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
  