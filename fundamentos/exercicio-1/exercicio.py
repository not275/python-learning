# 1 - Escreva um programa que lê dois nomes e retorne uma string formata no formato "ÚltimoNome, PrimeiroNome"
primeiroNome = input("digite o primeiro nome: ")
segundoNome = input("digite o segundo nome: ")
print(f"{segundoNome.capitalize()}, {primeiroNome.capitalize()}")

# 2 - Inverta a ordem das palavras em uma string fornecida
textoDigitado = input("digite um texto: ")
palavras = textoDigitado.split()
print(f"{" ".join(palavras[::-1])}")

# 3 - Verifique se uma string fornecida é um palíndromo (pode ser lida da mesma forma de trás pra frente)
texto1 = "ar ARA"
texto2 = "sol"
texto1Formatado = texto1.lower().replace(' ', '')
texto2Formatado = texto2.lower().replace(' ', '')

print(f"O texto {texto1Formatado} é um palíndromo? {texto1Formatado[::-1] == texto1Formatado}")
print(f"O texto {texto2Formatado} é um palíndromo? {texto2Formatado[::-1] == texto2Formatado}")
