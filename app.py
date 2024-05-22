import os
from flask import Flask
from flask_cors import CORS
from blueprints import register_blueprints
from extensions import db, migrate
from config import app_config, app_active

def create_app():
    config = app_config[app_active]

    app = Flask(__name__)  
    CORS(app)  

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config.APP = app

    db.init_app(app)
    migrate.init_app(app, db)

    from entities.cnae import Cnae
    from entities.empresa import Empresa
    from entities.empresa_cnae import EmpresaCnae
    from entities.qualificacao import Qualificacao
    from entities.socio import Socio
    from entities.socio_empresa import SocioEmpresa
    from entities.natureza_juridica import NaturezaJuridica
    from entities.endereco import Endereco, Municipio, Pais, Uf
    from entities.estabelecimento import Estabelecimento 
    from entities.motivo_situacao import MotivoSituacao

    app = register_blueprints(app)
    return app
