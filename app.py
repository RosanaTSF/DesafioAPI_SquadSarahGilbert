from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data_one = response.read()
    data = json.loads(data_one)
    
    return render_template("characters.html", characters=data["results"])


@app.route("/episodio/")
def get_episode():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data_two = response.read()
    data = json.loads(data_two)
    
    # Extrai a lista de episódios do objeto JSON
    episodios = data.get('results', [])
    
    return render_template("episode.html", episodio=episodios)


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
        characters.append(character_info) #
        
    return {"characters": characters}