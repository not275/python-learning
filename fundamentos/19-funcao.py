"""
    funções são estruturas em Python que permitem 
    reutilizar código e ter uma maior controle da 
    aplicação deixando o código mais legível
"""

movies = ["Inception", "Jurassic Park", "Titanic"]

#imprimir filmes utilizando uma função básica
print(f"imprimir filmes utilizando uma função simples")
def imprimirFilmes():
    print(f"a lista de filmes disponíveis é: {movies}")

imprimirFilmes()

#imprimir filmes utilizando uma função básica
print(f"\nimprimir filmes por nome utilizando uma função simples com retorno")
def buscarFilmesPorNome():
    termo = input("digite um termo para pesquisar filmes: ")
    retornoFilmes = [movie for movie in movies if termo.lower() in movie.lower()]

    if len(retornoFilmes) < 1:
        print(f"nenhum filme encontrado com o termo {termo}.")
    else:
        print(f"{len(retornoFilmes)} filme(s) encontrado(s) com o termo {termo}.")

    return retornoFilmes

retornoFilmes = buscarFilmesPorNome()

if retornoFilmes:
    for indice, movie in enumerate(retornoFilmes):
        print(f"{indice + 1}º resultado: {movie}")

#aplicação siples para cadastrar filmes utilizando funções básicas
print(f"\ncadastrar uma lista de filmes por função")

moviesCadastro = []

def pausar():
    input("\ndigite enter para continuar...")

def cadastrar():
    nome = input("digite o nome do filme: ")
    yearRelease = int(input("digite o ano de lançamento do filme: "))
    rating = float(input("digite a nota do filme: "))
    price = float(input("digite o preço do filme: "))

    moviesCadastro.append({
        "nome": nome,
        "ano": yearRelease,
        "nota": rating,
        "preco": price
    })

    print(f"filme: {moviesCadastro[-1]} cadastrado com sucesso!")
    pausar()

def listar():
    for indice, filme in enumerate(moviesCadastro):
        print(f"{indice + 1}: {filme["nome"]} ({filme["ano"]}) - {filme["nota"]:.2f} R$ {filme["preco"]:.2f}")

    if len(moviesCadastro) == 0:
        print(f"\nnenhum filme cadastrado no momento.")

    pausar()    

def remover():
    termo = input("digite o nome do filme para remover: ")
    resultados = [filme for filme in moviesCadastro if termo.lower() in filme["nome"].lower()]
    if resultados:
        print(f"\n{len(resultados)} resultados encontrados com o termo '{termo}")

        for indice, resultado in enumerate(resultados):
            if(indice == 0): 
                print(f"opcao[0] - voltar")

            print(f"opcao[{indice + 1}] - remover: {resultado["nome"]}")

        index = int(input("digite a opção para remover: ")) - 1
        
        if (index >= 0) and (index < len(moviesCadastro)):
            moviesCadastro.pop(index)
            print(f"\nfilme {resultados[index]["nome"]} excluído com sucesso!")
    else:
        print(f"\nnenhum resultado encontrado com o termo {termo}!")
    pausar()

while True:
    print(f"\nPrograma para cadastro de Filmes".center(20, '-'))
    print(f"".center(20, '-'))
    print(f"1 - cadastrar um novo filme")
    print(f"2 - listar filmes cadastrados")
    print(f"3 - remover um filme cadastrado")
    print(f"4 - sair do programa")
    print(f"".center(20, '-'))
    selecao = input("selecione a opção desejada: ")

    if selecao == '1':
        cadastrar()

    if selecao == '2':
        listar()

    if selecao == '3':
        remover()

    if selecao == '4':
        print(f"programa finalizando...")
        pausar()
        break