"""
    Os laços de repetição são importantes em qualquer aplicação
    neles é possível criar um ciclo de execução para tarefas 
    que precisa ser realizadas mais de uma vez, sem a repetição
    de código.
    Uma das estruturas mais utilizadas para este fim é o for.
"""
movies = ["Inception", "Jurassic Park", "Titanic"]

#percorrer uma lista de filmes:
print(f"\nexemplo: uso de for padrão")
for movie in movies:
    print(f"O nome do filme é: {movie}")

#percorrer uma lista com índice:
print(f"\nexemplo: uso de índice")
for i, movie in enumerate(movies):
    print(f"O nome do {i + 1}º filme é: {movie}")

#parar uma iteração com condição utilizando break
print(f"\nexemplo: uso de break")
for movie in movies:
    if movie == "Titanic":
        break
    else: 
        print(f"o nome do filme é {movie}")

#pular uma iteração com condição utilizando break
print(f"\nexemplo: uso de continue")
for movie in movies:
    if movie == "Inception":
        continue
    else:
        print(f"o nome do filme é {movie}")

#definir o número de iterações conforme input do usuário
print(f"\nexemplo: uso de uso de range")
nome = input("digite o nome do filme: ")
iteracoes = int(input("digite o número de avaliações: "))
resultado = 0

#range por padrão começa no 0, mas podemos definir um índice de início
for indice in range(iteracoes):
    nota = int(input(f"digite a {indice + 1}ª avaliação: "))
    resultado += nota

if iteracoes <= 1:
    print(f"a média das notas do filme {nome.title()} é: {resultado:.2f}.")
else:
    print(f"a média das notas do filme {nome.title()} é: {(resultado / iteracoes):.2f}.")