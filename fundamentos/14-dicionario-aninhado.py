"""
    dicionários aninhados é um dicionário com
    uma lista de dicionários internos, lembra 
    muito o multivalue map.
"""

import pprint

dictAninhado = {
    "The Matrix": {
        "yearRelease": 2000,
        "imdbRating": 8.9,
        "genre": ("action", "sci-fi", "thriller")
    }, 
    "Inception": {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ("action", "sci-fi", "thriller")
    },
    "Interstellar": {
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ("drama","sci-fi")
    }
}

print(f"este dicionario {dictAninhado} está aninhado")
print(f"o primeiro índice do dicionario {dictAninhado} é um {type(dictAninhado["The Matrix"])}")

#utilizar o módulo pprint para deixar a visualização do dicionário aninhado mais legível
pp = pprint.PrettyPrinter(depth=5) #depth é até qual nível deve ser apresentada as informações.
print(f"esta é a visualização mais bonita do dicionario")
pp.pprint(dictAninhado)

#acessar uma propriedade aninhada do dicionário interno
print(f"os gêneros do filme interstellar são {dictAninhado['Interstellar']['genre']}")

#adicionar um novo item dentro de um dicionário aninhado
dictAninhado["The Matrix"]['director'] = ("Lana Wachowski", "Lilly Wachowski")
print(f"os diretores do filme matrix são {dictAninhado['The Matrix']['director']}")

#remover um dicionário dentro de outro dicionário
del dictAninhado["Interstellar"]
print(f"resultado do dicionário aninhado após a exclusão do filme interstellar")
pp.pprint(dictAninhado)