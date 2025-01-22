#strings em Python são case sensitive
name = "Abc"
name2 = "abc"
print(f"{name} é igual a {name2}? {name == name2}")

#string multilinha obedecem o mesmo posicionamento que foi digitado
print(f"\nExemplo de String Multilinha:")
stringMultilinha = """
    Estou estudando Python
    para trabalhar com
IA
"""
print(stringMultilinha)

#multiplacação de string, podemos adicionar um multiplicador para repetir uma determinada string n vezes.
#multiplicação direta:
print("=" * 50)
#ou declarando uma variável:
line = "="
print(line * 50)

#procurar um texto dentro de uma string, é case sensitive:
print(f"\no texto 'a' está contido em name? {"a" in name}")
print(f"o texto 'A' está contido em name? {"A" in name}")
print(f"o texto 'IA' está contido em stringMultinha? {"IA" in stringMultilinha}")
print(f"o texto 'AI' está contido em stringMultinha? {"AI" in stringMultilinha}")
print(f"o texto 'to' está contido em stringMultinha? {"to" in stringMultilinha}") #parte de uma palavra