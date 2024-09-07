from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

URLBASE = "https://rickandmortyapi.com/api"

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
# Rota principal que exibe a lista de personagens
@app.route("/")
def get_list_characters_page():
    page = int(request.args.get('page', 1)) # /?page=1
    url = f"{URLBASE}/character?page={page}"
    response = urllib.request.urlopen(url)
    data_one = response.read()
    data = json.loads(data_one)

    pagination = pagination_att(page, data, '/')
    
    return render_template("characters.html", characters=data["results"], pagination=pagination)

# Rota que exibe a lista de episódios
@app.route("/episodes/")
def get_episode():
    page = int(request.args.get('page', 1)) # /?page=1
    url = f"{URLBASE}/episode?page={page}"
    response = urllib.request.urlopen(url)
    data_two = response.read()
    data = json.loads(data_two)

    pagination = pagination_att(page, data, '/episodes')

    return render_template("episodes.html", episodes=data["results"] ,pagination=pagination)

# Rota que exibe a lista de episódios
@app.route("/episodes/<id>")
def get_episode_id(id):
    url = f"{URLBASE}/episode/{id}"
    response = urllib.request.urlopen(url)
    data_two = response.read()
    data = json.loads(data_two)

    return render_template("episode.html", episode=data)

@app.route("/profile/<id>") 
def get_profile(id):
    url = f"{URLBASE}/character/{id}"
    try:
        response = urllib.request.urlopen(url)
        data_one = response.read()
        data = json.loads(data_one)
    except Exception as e:
        return f"Erro ao buscar dados: {e}", 500
    
    return render_template("profile.html", profile=data)

@app.route("/locations/")
def get_locations():
    page = int(request.args.get('page', 1)) # /?page=1
    url = f"{URLBASE}/location?page={page}"
    #url = f"{URLBASE}/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    pagination = pagination_att(page, dict, '/locations')
    return render_template("locations.html",locations=dict["results"], pagination=pagination)

@app.route("/locations/<id>")
def get_locations_id(id):
    url = f"{URLBASE}/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("location.html",location=dict)

# Rota que retorna uma lista de personagens simplificada em JSON
@app.route("/lista")
def get_list_elements():
    url = f"{URLBASE}"
    response = urllib.request.urlopen(url)
    characters_data = response.read()
    data = json.loads(characters_data)

    return data