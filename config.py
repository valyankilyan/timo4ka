import os
from dotenv import load_dotenv

load_dotenv()

# basedir = os.path.apspath(os.path.dirname(__file__))

class FlaskConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-very-secret-key'
    
min_side = 10
max_side = 1600
tima_path = 'tima_images'