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

'''
@app.route('/templates/')
def import_actors():
    first_name = request.form['import_firstname']
    last_name = request.form['import_lastname']
    print("First name : ", first_name, " et last name ", last_name)
    return 'Submitted!'
'''

def test():
    #convertir un dictionnaire en un JSON puis le renvoie sous forme de reponse HTTP
    dictionnaire = {
        'title': 'La nuit du 12',
        'director': 'Dominik Moll',
        'year': 2021,
        'actors': ["Bastion Bouillon", "Theo Cholbi", "Julien Frison"]
    }
    return jsonify(dictionnaire)

    """
    Qd le client appellera l'endpoint /api/test/ le programme Python enverra une requete vers l'API REST (A FAIRE)
    On stocke la reponse de REST dans la variable response, on les convertit en dictionnaire Python grace a json.loads
    si elle fonctionne renvoie 200
    """
    #response = requests.get(VIDEO_API_URL)
    #content = json.loads(response.content.decode('utf-8'))
    """
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requete a l\'API REST(?) n\'a pas fonctionne. Voici le message renvoye par l\'API : {}'.format(content['message'])
        }), 500
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
