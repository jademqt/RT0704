#-*- coding: utf-8 -*- 

import requests
import json
from flask import Flask, jsonify, render_template, redirect, url_for, request, session
from apicalls import *

app = Flask(__name__)

rest_full_address = "http://172.17.0.2:8000/"

persons_list = []
movies_list = []
lib_list = []

def update_lists():
    global persons_uri_list
    persons_uri_list = get_persons_list()
    global movies_uri_list
    movies_uri_list = get_movies_list()
    global lib_uri_list
    lib_uri_list = get_vlib_list()

def create_persons_list():
    update_lists()
    persons_list.clear()
    for per in persons_uri_list :
        persons_list.append(per[12:])

def create_movies_list():
    update_lists()
    movies_list.clear()
    for mov in movies_uri_list :
        movies_list.append(mov[11:])

def create_videolib_list():
    update_lists()
    lib_list.clear()
    for lib in lib_uri_list :
        lib_list.append(lib[9:])

@app.route('/')
def web():
    print("[x] access to /")
    return  render_template("index.html")

@app.route('/import_actors')
def import_actors():
    return render_template("import_actors.html")

@app.route('/import_movies', methods=['GET'])
def import_movies():
    create_persons_list()
    return render_template('import_movies.html', persons_list=persons_list)

@app.route('/import_videolib', methods=['GET'])
def import_videolib():
    create_persons_list()
    create_movies_list()
    return render_template('import_videolib.html', persons_list=persons_list, movies_list=movies_list)

@app.route('/import_owner')
def import_owner():
    return render_template('import_owner.html')

@app.route('/delete_actors', methods=['GET'])
def delete_actors():
    create_persons_list()
    return render_template("delete_actors.html", persons_list=persons_list)

@app.route('/delete_movies', methods=['GET'])
def delete_movies():
    create_movies_list()
    return render_template('delete_movies.html', movies_list=movies_list)

@app.route('/delete_videolib', methods=['GET'])
def delete_videolib():
    create_videolib_list()
    return render_template('delete_videolib.html', lib_list=lib_list)

@app.route('/explore_actors')
def explore_actors():
    update_lists()
    full_list = []
    person_tup = ()
    long=0
    for u in persons_uri_list:
        jsobj = json.loads(get_person(u).content)
        person_tup = (jsobj['first_name'], jsobj['last_name'], jsobj['tag'])
        if person_tup[2]=="actor" :
            full_list.append(person_tup)
        long = len(full_list)

    return render_template("explore_actors.html", long=long, flist = full_list)


@app.route('/explore_movies')
def explore_movies():
    update_lists()
    full_list = []
    movie_tup = ()
    long=0
    for u in movies_uri_list:
        jsobj = json.loads(get_movie(u).content)
        movie_tup = (jsobj['title'], jsobj['year'])
        full_list.append(movie_tup)
        long = len(full_list)
    return render_template('explore_movies.html', long=long, full_list=full_list)


@app.route('/explore_videolib')
def explore_videolib():
    update_lists()
    full_list = []
    vlib_tup = ()
    long=0
    for v in lib_uri_list:
        jsobj = json.loads(get_vlib(v).content)
        vlib_tup = (jsobj['title'], jsobj['owner'][12:])
        full_list.append(vlib_tup)
        long = len(full_list)
    return render_template('explore_videolib.html', long=long, flist = full_list)


@app.route('/actor_created', methods=['POST', 'GET'])
def actor_created():
    first_name = request.form.get('import_firstname')
    last_name = request.form.get('import_lastname')

    res = new_person(first_name, last_name, "actor") 
    update_lists()
    return render_template("actor_created.html", first_name=first_name, last_name=last_name)

@app.route('/owner_created', methods=['POST', 'GET'])
def owner_created():
    owner_first_name = request.form.get('owner_first_name')
    owner_last_name = request.form.get('owner_last_name')
    #rajouter condition
    res = new_person(owner_first_name, owner_last_name, "owner")
    update_lists()
    return render_template("owner_created.html",  owner_first_name=owner_first_name, owner_last_name=owner_last_name)

@app.route('/movie_created', methods=['POST', 'GET'])
def movie_created():
    title = request.form.get('title')
    director = request.form.get('director')
    movie_year = request.form.get('movie_year')
    movie_actors = request.form.getlist('movie_actors')

    res = new_movie(title, director, movie_year, movie_actors).content
    if res == "NOK":
        print("yo wtf dawg")

    return render_template("movie_created.html", title=title, director=director, movie_year=movie_year, movie_actors=movie_actors)

@app.route('/videolib_created', methods=['POST', 'GET'])
def videolib_created():
    videolib_title = request.form.get('videolib_title')
    owner = request.form.get('owner')
    videolib_movies = request.form.getlist('videolib_movies')

    res = new_vlib(videolib_title, owner, videolib_movies)
    if res == "NOK":
        print("BIZARRE")

    return render_template("videolib_created.html", videolib_title=videolib_title, owner=owner, videolib_movies=videolib_movies)

@app.route('/actor_deleted', methods=['POST', 'GET'])
def actor_deleted():
    actor_to_del = request.form.get('actor')
    res = del_person(actor_to_del)
    if res == 'NOK' :
        print('erreur dans actor_deleted')
    else:
        print(actor_to_del + ' has been deleted with success ')
        update_lists()
    return render_template("actor_deleted.html", actor_to_del=actor_to_del)

@app.route('/movie_deleted', methods=['POST', 'GET'])
def movie_deleted():
    movie_to_del = request.form.get('movie')
    res = del_movie(movie_to_del)
    if res == 'NOK' :
        print('erreur dans movie_deleted')
    else :
        print(movie_to_del + ' has been deleted with success ')
        update_lists()
    return render_template('movie_deleted.html', movie_to_del=movie_to_del)

@app.route('/videolib_deleted', methods=['POST', 'GET'])
def videolib_deleted():
    videolib_to_del = request.form.get('videolib')
    res = del_vlib(videolib_to_del)
    if res == 'NOK' :
        print('erreur dans videolib_deleted')
    else :
        print(videolib_to_del + ' has been deleted with success')
        update_lists()
    return render_template('videolib_deleted.html', videolib_to_del=videolib_to_del)

@app.route('/movie', methods=['GET'])
def template_movies():
    movie_chosen = request.args.to_dict()['mov']
    str_movie_chosen = get_movie("api/movies/" + movie_chosen.lower()).content
    final_movie = json.loads(str_movie_chosen)
    title = final_movie['title']
    director = final_movie['director']
    director = director[12:]
    year = final_movie['year']
    uri_list_actors = final_movie['actors']
    tab_list_actors = []
    for act in uri_list_actors :
        tab_list_actors.append(act[12:])

    return render_template('template_movies.html', title=title, director=director, year=year, tab_list_actors=tab_list_actors)

@app.route('/videolib', methods=['GET'])
def template_videolib():
    videolib_chosen = request.args.to_dict()['vid']
    str_videolib_chosen = get_movie("api/vlib/" + videolib_chosen.lower()).content
    final_videolib = json.loads(str_videolib_chosen)
    title = final_videolib['title']
    owner = final_videolib['owner'][12:]
    uri_list_movies = final_videolib['movies']
    tab_list_movies = []
    for mov in uri_list_movies :
        tab_list_movies.append(mov[11:])

    return render_template('template_videolib.html', title=title, owner=owner, tab_list_movies=tab_list_movies)

@app.route('/search', methods=['GET'])
def search_explore():
    return render_template('search.html')


@app.route('/template_search', methods=['GET', 'POST'])
def template_search():
    search_chosen = request.form.get('query')
    list_results = (search(search_chosen).content).decode()
    tab_object = []
    tab_category = []
    tab_uri = list_results.split("\n")[:-1]

    #debug
    app.logger.info("query : " + search_chosen)
    app.logger.info("tab_uri : " + str(tab_uri))

    for res in tab_uri :
        app.logger.debug("res : " + res)
        tab = res.split('/')
        tab_category.append(tab[1])
        tab_object.append(descriptor(res))
    long = len(tab_uri)
    return render_template('template_search.html',  tab_category=tab_category, tab_object=tab_object, long=long, search_chosen=search_chosen)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8001)
