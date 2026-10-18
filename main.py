import filmes as films

while True:
    print("Menu:")
    print("1. Buscar filmes")
    print("2. Buscar filme por título")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        films.buscarFilmes()
    elif opcao == "2":
        titulo = input("Digite o título do filme: ")
        films.buscarFilmePorTitulo(titulo)
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")