from flask import Flask, render_template, request, redirect, url_for

from handlers.utils import union_data
from db import sql
 

app = Flask(__name__)
# flask --app main.py run --debug

@app.route("/", methods = ['GET', 'POST'])
def index():
    """Главная страница"""
    if request.method == 'POST':
        title = request.form.get("title")
        watched = request.form.get("check")
        
        if watched is None:
            watched = 0
        else:
            watched = 1
        
        sql.update_data((watched, title))
        return redirect(url_for("index"))
        
    videos = union_data()  
    return render_template('home.html', videos=videos)