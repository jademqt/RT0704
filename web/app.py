#-*- coding: utf-8 -*- 
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
app = Flask(__name__)

@app.route('/')
def web():
    return  render_template("index.html")

@app.route('/import_actors')
def import_actors():
    return render_template("import_actors.html")

@app.route('/import_movies')
def import_movies():
    return render_template('import_movies.html')

@app.route('/import_videolib')
def import_videolib():
    return render_template('import_videolib.html')

@app.route('/import_owner')
def import_owner():
    return render_template('import_owner.html')

@app.route('/delete_actors')
def delete_actors():
    return render_template("delete_actors.html")

@app.route('/delete_movies')
def delete_movies():
    return render_template('delete_movies.html')

@app.route('/delete_videolib')
def delete_videolib():
    return render_template('delete_videolib.html')

@app.route('/explore_actors')
def explore_actors():
    return render_template("explore_actors.html")

@app.route('/explore_movies')
def explore_movies():
    return render_template('explore_movies.html')

@app.route('/explore_videolib')
def explore_videolib():
    return render_template('explore_videolib.html')


@app.route('/actor_created', methods=['POST', 'GET'])
def actor_created():
    first_name = request.form.get('import_firstname')
    last_name = request.form.get('import_lastname')
    return render_template("actor_created.html", first_name=first_name, last_name=last_name)

@app.route('/owner_created', methods=['POST', 'GET'])
def owner_created():
    owner_first_name = request.form.get('owner_first_name')
    owner_last_name = request.form.get('owner_last_name')
    return render_template("owner_created.html",  owner_first_name=owner_first_name, owner_last_name=owner_last_name)

@app.route('/movie_created', methods=['POST', 'GET'])
def movie_created():
    title = request.form.get('title')
    director = request.form.get('director')
    movie_year = request.form.get('movie_year')
    movie_actors = request.form.getlist('movie_actors')
    return render_template("movie_created.html", title=title, director=director, movie_year=movie_year, movie_actors=movie_actors)

@app.route('/videolib_created', methods=['POST', 'GET'])
def videolib_created():
    videolib_title = request.form.get('videolib_title')
    owner = request.form.get('owner')
    videolib_movies = request.form.getlist('videolib_movies')
    return render_template("videolib_created.html", videolib_title=videolib_title, owner=owner, videolib_movies=videolib_movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
