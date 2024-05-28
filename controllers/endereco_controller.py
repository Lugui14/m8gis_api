from flask import Blueprint, jsonify
from services.endereco_service import EnderecoService

endereco_blueprint = Blueprint('endereco', __name__, url_prefix='/endereco')
service = EnderecoService()

@endereco_blueprint.route('/', methods=['GET'])
def index():
  return jsonify(service.fill_lat_long())

@endereco_blueprint.route('/municipios', methods=['GET'])
def municipios():
  return jsonify(service.get_municipios())

@endereco_blueprint.route('/uf', methods=['GET'])
def uf():
  return jsonify(service.get_uf())