#-*- coding: utf-8 -*- 
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def web():
    return  render_template("/home/toto/RT0704/interface_web/index.html")

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
