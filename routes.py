from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

URLBASE = "https://rickandmortyapi.com/api"

# Rota principal que exibe a lista de personagens
@app.route("/")
def get_list_characters_page():
    url = f"{URLBASE}/character/"
    response = urllib.request.urlopen(url)
    data_one = response.read()
    data = json.loads(data_one)
    return render_template("characters.html", characters=data["results"])

# Rota que exibe a lista de episódios
@app.route("/episodio/")
def get_episode():
    url = f"{URLBASE}/episode"
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
    url = f"{URLBASE}/episode/{id}"
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

# sugestao para a rota de cima (Letícia):
# tirar a parte do for de characters e colocar logo no return o characters_urls, funciona da mesma forma

# e uma dúvida:
# as rotas episodio e episode/id poder renderizar o mesmo template? achei que faria mais sentido com templates diferentes

# Rota que retorna uma lista de personagens simplificada em JSON
@app.route("/lista")
def get_list_elements():
    url = f"{URLBASE}/character/"
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