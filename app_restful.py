
from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
        {
            "nome": "Gutierre",
            "habilidades": ['Python', 'Flask']
        },
        {
            "nome": "Thiago",
            "habilidades": ['Python', 'Django']
        },
        {
            "nome": "Guimarães",
            "habilidades": ['Python', 'Django']
        },
    ]

class Desenvolvedor(Resource):
    def get(self, id):

        try:
            response = desenvolvedores[id]

        except IndexError: 
            mensagem = "Desenvolvedor de ID {} não existe".format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        
        except Exception: 
            mensagem = "Erro deswconhecido, Procure o administrador da API"
            response = {'status': 'erro', 'mensagem': mensagem}

        print(response)
        return response

    def put(self, id):
        print(request.data)
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return {
            'dados': desenvolvedores[id],
            'mensagem': "Dados Alterados para: ",
            'novo_dados': dados
        }

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'success', 'mensagem': 'Registro excluido'}

class listaDesenvolvedores(Resource):
    def get(self): 
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(listaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
