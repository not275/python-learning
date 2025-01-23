"""
    É uma forma mais performática de iterar listas
    utilizando a estrutura da lista com um for interno
"""

movies = ["Inception", "Jurassic Park", "Titanic"]

#imprimindo a lista de filmes utilizando o list comprehension
print(f"exemplo de iteração da lista com list comprehension")
print(f"lista de filmes: {[movie for movie in movies]}")

#imprimindo a lista de filmes utilizando o list comprehension com range
print(f"exemplo de iteração da lista com list comprehension com range")
print(f"lista de números menores que 5: {[num for num in range(10) if num < 6]}")

#imprimindo uma lista de filmes com condicional
print(f"\nexemplo de iteração da lista com list comprehension com condição")
print(f"lista de filmes que contém 'ti' no nome: {[movie for movie in movies if 'ti' in movie.lower()]}")

#imprimindo uma lista de filmes com condicional por nome
print(f"\nexemplo de iteração da lista com list comprehension com condição por nome")
print(f"lista de filmes que eu assisti: {[movie for movie in movies if movie.lower() != 'jurassic park']}")

#imprimindo uma lista filtrando filmes por termo de busca:
print(f"\nexemplo de iteração da lista com list comprehension com filtro por nome")
while True:
    termo = input("digite um termo para buscar os filmes ou \sair para encerrar: ")
    if termo == '\sair' : break
    else:
        resultados = [movie for movie in movies if termo.lower() in movie.lower()]

    if resultados:
        print(f"foram encontrados resultados com o termo: {termo}")
        for indice, resultado in enumerate(resultados):
            print(f"o {indice + 1}º resultado encontrado: {resultado}")
    else:
        print(f"nenhum resultado encontrado com o termo {termo}")
    