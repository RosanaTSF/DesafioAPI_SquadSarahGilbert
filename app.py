from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

URLBASE = "https://rickandmortyapi.com/api"

# Rota principal que exibe a lista de personagens
@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data_one = response.read()
    data = json.loads(data_one)
    return render_template("characters.html", characters=data["results"])

# Rota que exibe a lista de episódios
@app.route("/episodio/")
def get_episode():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data_two = response.read()
    data = json.loads(data_two)
    episodios = data.get('results', [])
    return render_template("episode.html", episodios=episodios)

@app.route("/locations/")
def get_locations():
    url = f"{URLBASE}/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("locations.html",locations=dict["results"])

@app.route("/locations/<id>")
def get_locations_id(id):
    url = f"{URLBASE}/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("location.html",location=dict)

# Nova rota que exibe o perfil de um episódio específico
@app.route("/episode/<id>")
def episode_profile(id):
    # Faz a requisição para o episódio específico usando o ID
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    episode_data = response.read()
    episode = json.loads(episode_data)

    # Lista de personagens que aparecem no episódio
    character_urls = episode["characters"]
    characters = []

    # Busca dados de cada personagem no episódio
    for character_url in character_urls:
        char_response = urllib.request.urlopen(character_url)
        char_data = char_response.read()
        character = json.loads(char_data)
        characters.append(character)

    return render_template(
        "episode.html", 
        episode=episode, 
        characters=characters
    )

# Rota que retorna uma lista de personagens simplificada em JSON
@app.route("/lista")
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters_data = response.read()
    data = json.loads(characters_data)
    
    characters = []
    for character in data["results"]:
        character_info = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character_info)

    return {"characters": characters}

if __name__ == "_main_":
    app.run(debug=True)

    #Explicação da Nova Rota /episode/<id> URL Dinâmica: A rota é configurada para aceitar um parâmetro <id> que representa o ID do episódio. Requisição para o Episódio Específico: Faz uma requisição para a API usando o ID para obter detalhes do episódio. Lista de Personagens: Extrai a lista de URLs dos personagens que aparecem no episódio e faz requisições individuais para cada personagem para coletar os dados necessários. Renderização: Renderiza o template episode.html com as informações do episódio e a lista de personagens.(Rosana).