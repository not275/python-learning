"""
   O dicionário (Map) dict em Python é uma estrutura dinâmica 
   em forma de lista que guarda propriedades de chave e valor, 
   permitindo um detalhamento maior dos dados, lembra muito o json
"""

dictExample = {
    "title": "The Matrix",
    "yearRelease": 2000,
    "imdbRating": 8.9,
    "genre": ("action", "sci-fi", "thriller")
}

print(type(dictExample))
print(f"o dicionário {dictExample} tem {len(dictExample)} elementos")

#recuperar as informações do dicionário, duas formas:
print(f"o dicionário {dictExample} tem os seguintes generos {dictExample.get("genre")}")
print(f"o dicionário {dictExample} tem a seguinte nota no imdb: {dictExample["imdbRating"]}")

#retornar chaves do dicionário
print(f"o dicionário tem as seguintes chaves: {dictExample.keys()}")

#retornar os valores do dicionário
print(f"o dicionário tem os seguintes valores: {dictExample.values()}")

#retornar os itens com chave e valor do dicionário
print(f"o dicionário tem os seguintes itens: {dictExample.items()}")

#adicionar um novo valor no dicionário
dictExample["director"] = ("Lana Wachowski", "Lilly Wachowski")
print(f"o dicionário tem o seguinte valor para diretor {dictExample.get('director')}")

#atualizar um valor no dicionário
dictExample.update({"imdbRating": 9.0})
print(f"o valor da nota imdb atualizada é {dictExample.get("imdbRating")}")

#remover um valor no dicionário
dictExample.pop("director")
print(f"os itens do dicionário {dictExample} após a remoção do valor de diretor")