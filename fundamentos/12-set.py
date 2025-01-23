"""
    o Set é uma lista com valores únicos,
    uma curiosidade deste tipo é que valores
    0 e 1 são considerados o mesmo valor (False e True)
    Set assim como lista pode ter valores heterogêneos,
    Set não possui uma ordenação específica
"""
listaSet = {"filme 1", "filme 2", "filme 3", "filme 4"}

print(type(listaSet))

#obter número de elementos do set
print(f"o set {listaSet} tem {len(listaSet)} elementos")

#criar um novo set com elementos heterogêneos
outroSet = {"filme 2", True, 8.5}
print(f"o outro set tem os seguintes valores {outroSet}")

#atualizar um set com elementos de outro set -> valores duplicados não são considerados
listaSet.update(outroSet);
print(f"após obter os valores do set {outroSet} agora o listaSet tem os seguintes elementos: {listaSet}")

#remover um elemento do set pelo valor
listaSet.remove(True)
listaSet.remove(8.5)
print(f"após a remoção dos valores agora o set {listaSet} tem {len(listaSet)} elementos")