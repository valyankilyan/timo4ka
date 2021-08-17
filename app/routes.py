from loggerconfig import getLogger
log = getLogger(__name__)

from flask import render_template, redirect, flash, request
from app import app
import config
from PIL import Image
import random
from os import listdir


@app.route('/')
def index():
    getTimaImage()
    return render_template('index.html', title='Главная')


def getTimaImage():
    image = get_random_image()
    width = randomSide()
    height = randomSide()
    rotation = getRotation()
    
    print(width, height, rotation)
    new_image = image.resize((width, height))
    print("resize")
    new_image = new_image.rotate(rotation)
    print("rotate")
    new_image.save('app/static/new_image.jpg')

def get_random_image():
    photos = listdir(config.tima_path)
    ph = photos[random.randint(0, len(photos)-1)]
    return Image.open(config.tima_path + '/' + ph)

def randomSide():
    return random.randint(config.min_side, config.max_side)

def getRotation():
    return random.randint(0, 360)

@app.route('/about')
def about():
    return render_template('about.html', title='О проекте')

@app.errorhandler(400)
def bad_request_error(error):
    flash('Кажется, что-то пошло не так..')
    return redirect('/')

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('error-401.html'), 401

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('error-403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error-404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('error-500.html'), 500