"""
    Vamos utilizar algumas funções para manipulação de listas
"""

lista = ["filme 1", "filme 2", "filme 3", "filme 4"]

#obter o tamanho da lista
print(f"a lista {lista} tem {len(lista)} elementos")

#obter um índice pelo valor
print(f"o elemento com o nome 'filme 2' está no índice {lista.index('filme 2')}")

#copiar uma lista para outra lista
listaCopiada = lista.copy()
print(f"a lista copiada {listaCopiada} e a lista {lista} são iguais? {listaCopiada == lista}")

#adicionar um novo elemento a lista
listaCopiada.append("filme 0")
print(f"a lista copiada {listaCopiada} agora tem {len(listaCopiada)} elementos")

listaCopiada.sort()
print(f"a lista copiada {listaCopiada} foi ordenada com sucesso")

#remover um elemento da lista pelo valor
listaCopiada.remove("filme 4")
print(f"a lista copiada {listaCopiada} removeu um item e agora tem {len(listaCopiada)} elementos")

#limpa uma lista
listaCopiada.clear()
print(f"a lista copiada {listaCopiada} removeu todos elementos agora tem {len(listaCopiada)} elementos")