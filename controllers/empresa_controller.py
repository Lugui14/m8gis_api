from flask import Blueprint, jsonify
from entities.empresa import Empresa

empresa = Blueprint('empresa', __name__, url_prefix='/empresa')

@empresa.route('/', methods=['GET'])
def get():
  return jsonify(Empresa.query.all())