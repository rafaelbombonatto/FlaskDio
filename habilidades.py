from flask_restful import Resource

lista_habilidades = [
    'python',
    'java',
    'flask',
    'php'
]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
