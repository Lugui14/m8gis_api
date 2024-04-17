from flask import Blueprint, jsonify
from services.natju_service import NatjuService

natju_blueprint = Blueprint('natju', __name__, url_prefix='/natju')
natjuService = NatjuService()

@natju_blueprint.route('/', methods=['GET'])
def get():
  return jsonify(natjuService.get_all())