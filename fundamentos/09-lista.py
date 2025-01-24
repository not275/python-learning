"""
    lista, diversos valores dentro de uma mesma variável, 
    podemos trabalhar com valores heterogêneos também.
"""

listaHeterogenea = ["filme 1", 2000, 5.0, True]
print(type(listaHeterogenea))
print(f"exemplo de lista com valores heterogêneos: {listaHeterogenea}")

listaHomogenea = ["filme 1", "filme 2", "filme 3", "filme 4"]
print(f"exemplo de lista com valores homogêneos: {listaHomogenea}")

#os exemplos aqui valem para lista homogêneas e heterogêneas
#obter apenas os dois primeiros índices da lista
print(f"primeiros dois filmes da lista: {listaHomogenea[:2]}")

#obter o último filme da lista
print(f"último filme da lista: {listaHomogenea[-1]}")

#obter um filme em um determinado índice
print(f"o segundo filme da lista: {listaHomogenea[1:2]}")

#obter filmes intermediários da lista
print(f"os filmes intermediários da lista: {listaHomogenea[1:3]}")
