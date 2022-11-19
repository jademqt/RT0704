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
def import_movies():
    return render_template('import_videolib.html')

@app.route('/import_owner')
def import_movies():
    return render_template('import_owner.html')

@app.route('/delete_actors')
def import_actors():
    return render_template("delete_actors.html")

@app.route('/delete_movies')
def import_movies():
    return render_template('delete_movies.html')

@app.route('/delete_videolib')
def import_movies():
    return render_template('delete_videolib.html')

@app.route('/explore_actors')
def import_actors():
    return render_template("explore_actors.html")

@app.route('/explore_movies')
def import_movies():
    return render_template('explore_movies.html')

@app.route('/explore_videolib')
def import_movies():
    return render_template('explore_videolib.html')


@app.route('/actor_created')
def import_actors():
    first_name = request.form['import_firstname']
    last_name = request.form['import_lastname']
    return render_template('actor_created.html')
    return first_name + " " + last_name



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
