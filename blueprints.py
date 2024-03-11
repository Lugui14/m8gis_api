from controllers.controller import route


def register_blueprints(app):
  app.register_blueprint(route, url_prefix='/')