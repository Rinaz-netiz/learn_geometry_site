from flask import Flask
from flask import render_template
from config.config import config

from handlers.videos_from_vk import get_videos

app = Flask(__name__)
# flask --app main.py run

@app.route("/")
def index():
    """Главная страница"""
    return render_template('home.html', videos=get_videos(config.vk_token))
