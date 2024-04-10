from flask import Blueprint, jsonify
from services.cnae_service import CnaeService

cnae_blueprint = Blueprint('cnae', __name__, url_prefix='/cnae')
cnaeService = CnaeService()

@cnae_blueprint.route('/', methods=['GET'])
def get():
  return jsonify(cnaeService.get_all())