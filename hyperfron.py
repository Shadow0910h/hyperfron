import requests

def testar_vulnerabilidade():
    while True:
        url = input("Digite a URL do site que você deseja testar: ")
        # Verifica se a URL é válida
        if not url.startswith('http'):
            url = 'https://' + url

        # Faz uma requisição GET para a URL
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            print(f"A URL {url} é vulnerável a ataques.")
        else:
            print(f"A URL {url} não é vulnerável a ataques.")
        # Pergunta se o usuário deseja testar outra URL
        resposta = input("Deseja testar outra URL? (s/n): ")
        if resposta.lower() != "s":
            break

# Exemplo de uso
testar_vulnerabilidade()
