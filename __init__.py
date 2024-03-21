from app import create_app
from config import app_config, app_active
from dotenv import load_dotenv

config = app_config[app_active]
load_dotenv(override=True)

if __name__ == '__main__':
    app = create_app()
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
