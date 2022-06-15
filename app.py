import json
from flask import Flask, jsonify, request

app = Flask(__name__)

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


@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            desenvelvedor = desenvolvedores[id]
        except IndexError: 
            desenvelvedor = desenvolvedores
        print(desenvelvedor)
        return jsonify(desenvelvedor)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        try:
            desenvolvedores[id] = dados
        except IndexError: 
            desenvolvedores.append(dados)
        return jsonify(dados)
        
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'success', 'mensagem': 'Registro excluido'})
    
    else: 
        return jsonify({'status': 'danger', 'mensagem': 'Erro'})


@app.route('/<id>')
def pessoas(id):
    return {'id': id,'nome': 'Gutierre', 'profissao': 'Desenvolvedor'}

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    print(dados)
    total = sum(dados['valores'])
    return jsonify( { "soma" : total } )

if __name__ == "__main__":
    app.run(debug=True)