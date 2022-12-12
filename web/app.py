#-*- coding: utf-8 -*- 

import requests
import json
from flask import Flask, jsonify, render_template, redirect, url_for, request, session
from datetime import timedelta
from apicalls import *

app = Flask(__name__)

persons_uri_list = []
movies_uri_list = []
vlib_uri_list = []

# load config
with open("/home/toto/RT0704/config.json", "r") as f:
    config = json.load(f)

rest_full_address = "http://" + config["rest_address"] + ":" + str(config["rest_port"]) + "/"

persons_uri_list = get_persons_list()
movies_uri_list = get_movies_list()
lib_uri_list = get_vlib_list()

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
    fname_list = []
    lname_list = []
    tag_list = []

    for u in persons_uri_list:
        jsobj = json.loads(get_person(u).content)
        fname_list.append(jsobj['first_name'])
        lname_list.append(jsobj['last_name'])
        tag_list.append(jsobj['tag'])

    return render_template("explore_actors.html", actor_pre = fname_list, actor_nom = lname_list, actor_tag = tag_list)

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

    res = new_person(first_name, last_name, "actor") 

    persons_uri_list = get_persons_list()
    
    return render_template("actor_created.html", first_name=first_name, last_name=last_name)

@app.route('/owner_created', methods=['POST', 'GET'])
def owner_created():
    owner_first_name = request.form.get('owner_first_name')
    owner_last_name = request.form.get('owner_last_name')
    
    res = new_person(owner_first_name, owner_last_name, "owner")

    persons_uri_list = get_persons_list()

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
    app.run(host=config["web_address"], port=config["web_port"], debug=True)
