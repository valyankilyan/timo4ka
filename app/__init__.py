import loggerconfig

log = loggerconfig.getLogger(__name__)

log.info("Starting application...")

import os
from flask import Flask
import config

def create_app():
    log.debug("Initializing Flask.")
    app = Flask(__name__)
    log.debug("Configurating Flask.")
    app.config.from_object(config.FlaskConfig)
    log.debug("Initializing CSRFProtection.")    
    return app

app = create_app()

from app import routes

log.info("Application started.")