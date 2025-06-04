from flask import Flask, request, jsonify
from flask_cors import CORS
from Descricao import gerar_descricao_produto

# Importando a função de geração de descrição do produto
app = Flask(__name__)
CORS(app)

# Configuração do CORS para permitir requisições de qualquer origem
@app.route('/gerar-descricao', methods=['POST'])
def gerar_descricao():
    data = request.get_json()
    nome_produto = data.get('nome_produto')
    if not nome_produto:
        # Se o nome do produto não for fornecido, retorna um erro
        return jsonify({'erro': 'Nome do produto não informado'}), 400
    descricao = gerar_descricao_produto(nome_produto)
    if descricao:
        # Se a descrição for gerada com sucesso, retorna a descrição
        return jsonify({'descricao': descricao})
    else:
        # Caso contrário, retorna um erro
        return jsonify({'erro': 'Erro ao gerar descrição'}), 500

if __name__ == '__main__':
    app.run(debug=True)