
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !\n"

@app.route('/index/')
def test_index():
    return render_template("index.html")

@app.route('/api/test/')
def test():
    #convertir un dictionnaire en un JSON puis le renvoie sous forme de réponse HTTP    dictionnaire = {
        'title': 'La nuit du 12',
        'director': 'Dominik Moll',
        'year': 2021,
        'actors': ["Bastion Bouillon", "Theo Cholbi", "Julien Frison"]
    }
    return jsonify(dictionnaire)

    """
    Qd le client appellera l'endpoint /api/test/ le programme Python enverra une re>    On stocke la réponse de REST dans la variable response, on les convertit en dic>    si elle fonctionne renvoie 200
    """
    #response = requests.get(VIDEO_API_URL)
    #content = json.loads(response.content.decode('utf-8'))
    """
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API REST(?) n\'a pas fonctionné. Voici le m>        }), 500
    """