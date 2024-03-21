from controllers.empresa_controller import empresa

def register_blueprints(app):
  app.register_blueprint(empresa)

  return app