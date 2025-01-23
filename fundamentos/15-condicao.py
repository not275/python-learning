"""
    As condições são tratamentos de fluxos
    para definir diferentes comportamentos
    em um aplicação. Essas condições podem
    ser por exemplo uma determinada entrada
    de dados que alteram o fluxo de execução
    da aplicação.
"""

#recebe entradas do usuário
name = input("digite o nome do filme: ")
year = int(input("digite o ano de lançamento do filme: "))
rating = float(input("digite a nota do filme: "))

if year > 2015 and rating > 8.0 :
    print(f"o filme {name} é recomendado.")
else:
    print(f"o filme {name} não é recomendado.")

num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))
operacao = input("digite a operação a ser realizada (+, -, *, /): ")

if operacao == '+':
    print(f"resultado: {num1} + {num2} = {(num1 + num2):.2f}.")
elif operacao == '-':
    print(f"resultado: {num1} - {num2} = {(num1 - num2):.2f}.")
elif operacao == '*':
    print(f"resultado: {num1} * {num2} = {(num1 * num2):.2f}.")
elif operacao == '/':
    if num2 > 0: 
        print(f"resultado: {num1} / {num2} = {(num1 / num2):.2f}.")
    else: 
        print(f"erro ao realizar a operação: divisão por zero.")
else:
    print(f"erro ao realizar a operação: operador inválido.")