from flask import Flask, render_template, request, url_for
from flask_sitemapper import Sitemapper
import urllib.request, json
import os

routes = [] 
sitemapper = Sitemapper()
app = Flask(__name__)
sitemapper.init_app(app)

URLBASE = "https://rickandmortyapi.com/api"

#Paginação
def pagination_att(page,data,endpoint):
    pagination = {}
    pagination["page"] = page
    pagination["first"] = f"{endpoint}?page={1}"
    if page == 1:
        pagination["prev"] = f"{endpoint}?page={1}"
        pagination["prev_pag"] = 1
    else:
        pagination["prev"] = f"{endpoint}?page={page-1}"
        pagination["prev_pag"] = page-1
    pagination["last"] = f"{endpoint}?page={data['info']['pages']}"
    pagination["last_num"] = data['info']['pages']
    if page == data['info']['pages']: #max == 42
        pagination["next"] = f"{endpoint}?page={data['info']['pages']}"
        pagination["next_pag"] = data['info']['pages']
    else:
        pagination["next"] = f"{endpoint}?page={page+1}"
        pagination["next_pag"] = page+1
    return pagination

#Rota principal que exibe a lista de personagens
@sitemapper.include(lastmod="2024-09-07")
@app.route("/")
def get_list_characters_page():
    page = int(request.args.get('page', 1)) # /?page=1
    url = f"{URLBASE}/character?page={page}"
    try:
        response = urllib.request.urlopen(url)
        data_one = response.read()
        data = json.loads(data_one)
        pagination = pagination_att(page, data, '/')

    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return render_template("characters.html", characters=data["results"], pagination=pagination)

#Rota do personagem 
@sitemapper.include(lastmod="2024-09-07")
@app.route("/profile/<id>") 
def get_profile(id):
    url = f"{URLBASE}/character/{id}"
    try:
        response = urllib.request.urlopen(url)
        data_one = response.read()
        data = json.loads(data_one)

    except Exception as e:
        return f"Erro ao buscar dados: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return render_template("profile.html", profile=data)

#Rota que exibe a lista de episódios
@sitemapper.include(lastmod="2024-09-07")
@app.route("/episodes/")
def get_episode():
    try:
        page = int(request.args.get('page', 1)) # /?page=1
        url = f"{URLBASE}/episode?page={page}"
        response = urllib.request.urlopen(url)
        data_two = response.read()
        data = json.loads(data_two)
        pagination = pagination_att(page, data, '/episodes')
    
    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return render_template("episodes.html", episodes=data["results"] ,pagination=pagination)

#Rota do episódio
@sitemapper.include(lastmod="2024-09-07")
@app.route("/episodes/<id>")
def get_episode_id(id):
    url = f"{URLBASE}/episode/{id}"
    try:
        response = urllib.request.urlopen(url)
        data_two = response.read()
        data = json.loads(data_two)

    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return render_template("episode.html", episode=data)

#Rota que exibe a lista dos planetas vs localização
@sitemapper.include(lastmod="2024-09-07")
@app.route("/locations/")
def get_locations():
    page = int(request.args.get('page', 1)) # /?page=1
    url = f"{URLBASE}/location?page={page}"
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        pagination = pagination_att(page, dict, '/locations')
    
    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500

    return render_template("locations.html",locations=dict["results"], pagination=pagination)

#Rota do planeta 
@sitemapper.include(lastmod="2024-09-07")
@app.route("/locations/<id>")
def get_locations_id(id):
    url = f"{URLBASE}/location/{id}"
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        
    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return render_template("location.html",location=dict)

# Rota que retorna uma lista de personagens simplificada em JSON
@app.route("/lista")
def get_list_elements():
    url = f"{URLBASE}"
    try:
        response = urllib.request.urlopen(url)
        characters_data = response.read()
        data = json.loads(characters_data)

    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
    
    return data

#Rota da documentação
@app.route("/documentation")
def documentation():
    url = f"{URLBASE}/documentation"
    #url_base = "http://127.0.0.1:5000"
    scheme = request.scheme  # 'http' ou 'https'
    host = request.host      # '127.0.0.1:5000' ou 'localhost:5000'
    url_base = f'{scheme}://{host}'

    dict_total= {}

    try:
        for var in ['character','location','episode']:
            url = f"{URLBASE}/{var}"
            response = urllib.request.urlopen(url)
            data_one = response.read()
            data = json.loads(data_one)
            dict_total[var] = data['info']['count']

        routes = [
            {
                "method": "GET",
                "url": f"{url_base}/",
                "description": "Mergulhe no multiverso de Rick e Morty! Descubra personagens, episódios e planetas."
            },
            {
                "method": "GET",
                "url": f"{url_base}/profile/1",
                "description": f"Descubra tudo sobre um personagem. São {dict_total['character']} personagens para você explorar!"
            },
            {
                "method": "GET",
                "url": f"{url_base}/episodes/",
                "description": "Explore a lista completa de episódios e descubra os mais emocionantes."
            },
            {
                "method": "GET",
                "url": f"{url_base}/episodes/1",
                "description": f"Descubra tudo sobre um episódio específico. São {dict_total['episode']} episódios para você explorar!"
            },
            {
                "method": "GET",
                "url": f"{url_base}/locations/",
                "description": "Explore a lista completa dos planetas mais bizarros do multiverso!"
            },
            {
                "method": "GET",
                "url": f"{url_base}/locations/1",
                "description": f"Descubra tudo sobre um planeta específico. São {dict_total['location']} planetas para você explorar!"
            }
        ]
            
    except Exception as e:
        return f"Erro: {e}\nEXCEÇÃO: {type(e).__name__}", 500
        
    return render_template("documentation.html", routes=routes)