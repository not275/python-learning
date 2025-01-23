"""
    Os laços de repetição são importantes em qualquer aplicação
    neles é possível criar um ciclo de execução para tarefas 
    que precisa ser realizadas mais de uma vez, sem a repetição
    de código.
    Uma das estruturas mais utilizadas para este fim é o while.
"""
movies = ["Inception", "Jurassic Park", "Titanic"]
indice = 0

#percorrendo uma lista com while
print(f"exemplo de while para percorrer uma lista")
while indice < len(movies):
    print(f"o {indice + 1}º filme da lista é: {movies[indice]}")
    indice += 1

indice = 0

#percorrendo uma lista com condição de parada - break
print(f"\nexemplo de while para percorrer uma lista com break")
while indice < len(movies):
    if movies[indice] == "Titanic":
        break
    else:
        print(f"o nome do {indice + 1}º é {movies[indice]}")
        indice += 1

indice = 0

#percorrendo uma lista com condição de avanço da iteração - continue
print(f"\nexemplo de while para percorrer uma lista com continue")
while indice < len(movies):
    if movies[indice] == "Inception":
        indice += 1
        continue
    else:
        print(f"o nome do {indice + 1}º filme é {movies[indice]}")
        indice += 1

indice = 0

#percorrendo uma lista com input do número de iterações
print(f"\nexemplo de while para percorrer uma lista com input de iteracoes")

filme = input("digite o nome do filme: ")
iteracoes = int(input("digite o número de avaliações: "))
resultado = 0

while indice < iteracoes:
    nota = float(input(f"digite a {indice + 1}ª nota: "))
    resultado += nota
    indice += 1

if iteracoes < 2:
    print(f"a média de avaliações para o filme {filme.title()} é {resultado:.2f}")
else:
    print(f"a média de avaliações para o filme {filme.title()} é {(resultado / iteracoes):.2f}")