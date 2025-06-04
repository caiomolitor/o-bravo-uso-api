import requests
from googletrans import Translator

API_KEY = "3aetqoEIwfCUKX8ebbSKfhbvu2jB09vdPuwt9Vp0"  

translator = Translator()
# Função para gerar a descrição do produto usando a API da Cohere
# A função recebe o nome do produto e retorna uma descrição detalhada em português
def gerar_descricao_produto(nome_produto):
    prompt = (
        f"Describe the product '{nome_produto}' in detail. Include memory, performance, features, color options, and other technical specifications."
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "command",  
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0.7
    }

# Chamada à API da Cohere

    response = requests.post("https://api.cohere.ai/v1/generate", headers=headers, json=data)

    if response.status_code == 200:
        texto_gerado = response.json()["generations"][0]["text"].strip()
        traducao = translator.translate(texto_gerado, dest='pt').text
        return traducao
    else:
        # Se a chamada à API falhar, exibe o erro
        print("Erro ao chamar a API da Cohere:", response.status_code)
        print(response.json())
        return None


# Entrada interativa
if __name__ == "__main__":
    produto = input("Digite o nome do produto para gerar a descrição: ")
    descricao = gerar_descricao_produto(produto)

# Exibir a descrição gerada
    if descricao:
        print("\nDescrição Gerada em Português:\n")
        print(descricao)
