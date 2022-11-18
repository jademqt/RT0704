#-*- coding: utf-8 -*- 
from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
app = Flask(__name__)

@app.route('/')
def web():
    return  render_template("index.html")

@app.route('/templates/')
def import_actors():
    first_name = request.form['import_firstname']
    last_name = request.form['import_lastname']
    print("First name : ", first_name, " et last name ", last_name)
    return 'Submitted!'

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
