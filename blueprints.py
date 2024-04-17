from controllers.empresa_controller import empresa_blueprint
from controllers.cnae_controller import cnae_blueprint
from controllers.natju_controller import natju_blueprint
from controllers.estabelecimento_controller import estabelecimento_blueprint


def register_blueprints(app):
  app.register_blueprint(empresa_blueprint)
  app.register_blueprint(cnae_blueprint)
  app.register_blueprint(natju_blueprint)
  app.register_blueprint(estabelecimento_blueprint)
  

  return app