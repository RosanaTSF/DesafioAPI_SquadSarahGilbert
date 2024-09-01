from routes import app

if __name__ == "_main_":
    app.run(debug=True)

    #Explicação da Nova Rota /episode/<id> URL Dinâmica: A rota é configurada para aceitar um parâmetro <id> que representa o ID do episódio. Requisição para o Episódio Específico: Faz uma requisição para a API usando o ID para obter detalhes do episódio. Lista de Personagens: Extrai a lista de URLs dos personagens que aparecem no episódio e faz requisições individuais para cada personagem para coletar os dados necessários. Renderização: Renderiza o template episode.html com as informações do episódio e a lista de personagens.(Rosana).