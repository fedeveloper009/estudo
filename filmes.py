import requests

url = "https://ghibliapi.vercel.app/films"

response = requests.get(url)

def buscarFilmes():
    if response.status_code == 200:
        filmes = response.json()
        for filme in filmes:
            print(f"Titulo: {filme['title']}")
            print(f"Descrição: {filme['description']}")
            print(f"Diretor: {filme['director']}")
            print(f"Produtor: {filme['producer']}")
            print(f"Ano de lançamento: {filme['release_date']}")
            print(f"Nota: {filme['rt_score']}")
            print("-" * 40)
    else:
        print("Erro ao buscar filmes. Código:", response.status_code)
def buscarFilmePorTitulo(titulo):
    if response.status_code == 200:
        filmes = response.json()
        for filme in filmes:
            if titulo.lower() in filme['title'].lower():
                print(f"Titulo: {filme['title']}")
                print(f"Descrição: {filme['description']}")
                print(f"Diretor: {filme['director']}")
                print(f"Produtor: {filme['producer']}")
                print(f"Ano de lançamento: {filme['release_date']}")
                print(f"Nota: {filme['rt_score']}")
                return
    else:
        print("Erro ao buscar filmes. Código:", response.status_code)