"""
    A tupla é uma lista imutável (constante) com valores fixos,
    possui limitações, por exemplo: não pode ser ordenada
    A tupla tem algumas vantagens por exemplo consome menos memória
    e tem um acesso mais rápido que listas pelo valor fixo.
"""

tupla = ("filme 1", "filme 2", "filme 3", "filme 4")
print(type(tupla))

#A tupla tem os mesmos métodos de fatiamento e de índice que a lista
#obter a contagem de elementos da tupla
print(f"a tupla {tupla} tem {len(tupla)} elementos")

#obter os valores da tupla
print(f"a tupla tem os seguintes elementos: {tupla[0:]}")

#obter o último elemento da tupla
print(f"o último elemento da tupla {tupla} é {tupla[-1]}")

#obter os dois últimos índices da tupla
print(f"os dois últimos elementos da tupla {tupla} são {tupla[2:4]}")

#obter apenas os dois primeiros índices da tupla
print(f"os dois primeiros elementos da tupla {tupla} são {tupla[0:2]}")

#obter o índice da tupla pelo valor no índice
print(f"o elemento da tupla {tupla} com o nome 'filme 2' está no índice {tupla.index("filme 2")}")