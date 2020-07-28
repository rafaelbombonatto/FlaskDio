from flask import Flask, jsonify, request

import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Rafael',
        'habilidades':['python','flask']

    },
    {
        'id':'1',
        'nome':'João',
        'habilidades':['python','django']
    }
]

@app.route("/dev/", methods=["GET","POST"])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({"status":"sucess","mensagem":"desenvolvedor criado com sucesso"})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

@app.route("/dev/<int:id>/", methods=["GET","PUT","DELETE"])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
            print(desenvolvedor)            
        except IndexError:
            response = {"status":"erro", "mensagem":"Desenvolvedor não existe"}   
        return jsonify(response)    
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados   
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)    
        return "desenvolvedor excluido"

@app.route("/<int:numero>")
def ola(numero):
    return jsonify({"numero":numero})

@app.route("/soma/<int:numero1>/<int:numero2>")
def soma(numero1, numero2):
    return jsonify({"soma":numero1+numero2})

@app.route("/multisoma", methods=["POST"])
def multisoma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({"soma":total})    

if __name__ == "__main__":
    app.run(debug=True)    