@app.route('/api/test/')
def test():
    #convertir un dictionnaire en un JSON puis le renvoie sous forme de r�ponse HTTP
    dictionnaire = {
        'title': 'La nuit du 12',
        'director': 'Dominik Moll',
        'year': 2021,
        'actors': ["Bastion Bouillon", "Theo Cholbi", "Julien Frison"]
    }
    return jsonify(dictionnaire)

    """
    Qd le client appellera l'endpoint /api/test/ le programme Python enverra une requ�te vers l'API REST (A FAIRE)
    On stocke la r�ponse de REST dans la variable response, on les convertit en dictionnaire Python gr�ce � json.loads
    si elle fonctionne renvoie 200
    """
    #response = requests.get(VIDEO_API_URL)
    #content = json.loads(response.content.decode('utf-8'))
    """
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requ�te � l\'API REST(?) n\'a pas fonctionn�. Voici le message renvoy� par l\'API : {}'.format(content['message'])
        }), 500
    """

if __name__ == "__main__":
    app.run(debug=True)