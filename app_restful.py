from flask import Flask, request
from flask_restful import Resource,Api
from habilidades import Habilidades
from models import Pessoas, Atividades
import json


app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
   
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'pessoa não encontrada'
            }    
        return response
    

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {
            'status':'sucesso',
            'mensagem':'Pessoa excluida'
        }

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'atividade':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id':atividade.id

        }
        return response


api.add_resource(Pessoa,'/pessoa/<string:nome>/')        
api.add_resource(ListaPessoas,'/pessoa/')  
api.add_resource(ListaAtividades,'/atividade/')  




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