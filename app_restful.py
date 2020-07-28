from flask import Flask, request
from flask_restful import Resource,Api
from habilidades import Habilidades
import json


app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
            print(response)            
        except IndexError:
            response = {"status":"erro", "mensagem":"Desenvolvedor não existe"}   
        except Exception:
            response = {"status":"erro", "mensagem":"Erro"}       
        return response    

    def post(self, id):
        pass

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados   
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)    
        return "desenvolvedor excluido"

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor,'/dev/<int:id>/')        
api.add_resource(ListaDesenvolvedores,'/dev/')        
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)