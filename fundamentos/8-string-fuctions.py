#funções de manipulação de strings

#transformar string para maiúsculo
print("abcd".upper())

#transformar string para minúsculo
print("abcd".lower())

#transformar apenas o primeiro caracter em maiúsculo
print("ab cd".capitalize())

#transformar o primeiro caracter de cada palavra em maiúsculo
print("ab cd".title())

#string centralizada com caractere de preenchimento
print("abcd".center(8, '-'))  #adiciona o preenchimento para atingir o número de caracteres digitado (padding)

#retornar o índice de um determinado caractere
print("abcd".find('c'))

#conta o número de caracteres se houver mais de um caractere igual
print("aaba".count('a'))

#substituir caracteres ou palavras
print("de matrix".replace('de', 'the'))

#separar uma string normal ou multilinha
print("""
olá, mundo,
Python
""".split(','))