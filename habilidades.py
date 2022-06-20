from flask_restful import Resource

listaHabilidades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return listaHabilidades
