from controllers.empresa_controller import empresa_blueprint

def register_blueprints(app):
  app.register_blueprint(empresa_blueprint)

  return app