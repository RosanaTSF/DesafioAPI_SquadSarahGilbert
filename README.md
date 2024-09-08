# DesafioAPI_SquadSarahGilbert

## Para rodar o projeto

Com a versão 3.11 para cima do python, execute os seguintes comandos: 

    pip install poetry 
    poetry install
    poetry run flask --app app run

## Sincronizando com o Repositório Remoto (Upstream)

1. **Adicionar o repositório remoto (upstream):**

   Se você ainda não adicionou o repositório remoto upstream, adicione-o com o comando:

   ```bash
        git remote add upstream <URL_DO_REPOSITORIO>
2. **Buscar atualizações do repositório upstream:**

        git fetch upstream

3. **Verificar as diferenças entre a branch local e a branch upstream**

        git log HEAD..upstream/main --oneline

4. **Mesclar as alterações do upstream na branch local:**

        git merge upstream/main

_Esses comandos permitem que você mantenha sua branch local atualizada com as últimas mudanças do repositório remoto (upstream)._

##Deploy
### O deploy foi feito no render com uma conta individual
https://desafioapi-squadsarahgilbert.onrender.com/