from fastapi import FastAPI


app = FastAPI()

# ex 1

data = {
    1: {'name': 'Alice', 'age': 30},
    2: {'name': 'Beatriz', 'age': 20},
    3: {'name': 'Carlos', 'age': 10}
}
# rota para ler os usuários cadastrados
@app.get('/users')
def get_users():
    return data

# a) Rota para o verbo GET: /users/{user_id}, que mostre o conteúdo do
# dicionário “data” de acordo com user_id.

@app.get('/users/{user_id}')
def get_users_by_id(user_id: int):
    return data[user_id]

# b) Defina a rota para o verbo POST: /users/, para criar um novo usuário
# a partir da chave name e age.

@app.post('/users')
def post_users(name: str, age: int):
    data[len(data) + 1] = {'name': name, 'age': age}
    return data

# c) Defina a rota para o verbo PUT: /users/{user_id}, para atualizar os
# dados do usuário a partir da chave user_id, name e age.

@app.put('/users/{user_id}')
def update_user(user_id: int, name: str, age: int):
    data[user_id] = {'name': name, 'age': age}
    return data

# d) Defina a rota para o verbo DELETE: /users/{user_id}, para remover
# os dados do usuário a partir da chave user_id.

@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    del data[user_id]
    return data


# Nesses exercícios foi possível compreender o uso dos quatro verbos http:
# get, post, put, delete

# 1) utilizando o get:
# a solicitação http get irá retornar a leitura de algum dado (READ do CRUD)

# rota: @app.get('/users')
# @ - decorator - utilizado para indicar que uma função imediatamente abaixo será invocada quando houver uma solicitação para uma determinada rota
# app - variável que recebe uma instância de um objeto da classe FastAPI
# .get - utilização do método get no objeto app
# ('/users') - definição da rota que responderá à requisição http

# def get_users():
#     return data

# essa é a função chamada pela solicitação get para a rota indicada, nesse caso ela apenas retorna os dados armazenados na variável data

# o mais comum é o retorno de dados em formato JSON

# 2) fazendo uma consulta get específica:

# @app.get('/users/{user_id}')
# def get_users_by_id(user_id: int):
#     return data[user_id]

# essa é uma rota dinâmica: utilizando chaves na rota, é possível informar um parâmetro que será passado como argumento para a função, dessa forma é possível filtrar uma consulta no dicionário data

# 3) incluindo dados no dicionário data (CREATE do CRUD):

# @app.post('/users')
# def post_users(name: str, age: int):
#     data[len(data) + 1] = {'name': name, 'age': age}
#     return data

# o método post não é diretamente acessado pelo navegador da mesma forma que o método get, para utilizá-lo é necessário que essa rota seja chamada por meio de um formulário HTML, porém o FastAPI tem uma rota de documentação interativa para facilitar o teste da rota bastando incluir /docs ao final do localhost

# essa rota requer parâmetros para a função, esses parâmetros serão utilizados para criar um novo dado no dicionário, e a chave para esses dados está sendo criado com lógica ao acessar o tamanho do dicionário e adicionando +1, assim criando novo conjunto chave: valor. 

# está sendo utilizado em um contexto sem banco de dados, nesse caso o mais correto é utilizar um id auto-gerado pelo bd

# 4) atualizando dados (UPDATE do CRUD)

# @app.put('/users/{user_id}')
# def update_user(user_id: int, name: str, age: int):
#     data[user_id] = {'name': name, 'age': age}
#     return data

# o método put está sendo solicitado no contexto de uma rota com filtro por id, que também só pode ser acessado via formulário no html.

# assim, o parâmetro da rota variável é passado para a função, que utilizará ele com a chave do dicionário, e assim irá acessar os dados, os demais parâmetros da função serão os valores passados como novos valores para aquela chave informada. 

# 5) deletando dados (DELETE do CRUD)

# @app.delete('/users/{user_id}')
# def delete_user(user_id: int):
#     del data[user_id]
#     return data

# da mesma forma que filtramos com GET, agora filtramos com delete