from flask import Flask
from flask import render_template
from config.config import config

from handlers.videos_from_vk import get_videos
from db import sql

app = Flask(__name__)
# flask --app main.py run --debug

@app.route("/")
def index(page=1):
    """Главная страница"""
    videos = get_videos(config.vk_token)
    
    return render_template('home.html', videos=videos)