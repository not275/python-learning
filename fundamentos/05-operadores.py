num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Operadores Aritméticos:
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
modulus = num1 % num2 #resto da divisão de num1 por num2 ex: 5/3 = 2
potencia = num1 ** num2 #multiplica o num1 por ele mesmo igual a quantidade de num2, ex: 5 ** 3 = 5*5*5

#Operadores Comparação:
maior = num1 > num2
menor = num1 < num2
maiorIgual = num1 >= num2
menorIgual = num1 <= num2
igual = num1 == num2
diferente = num1 != num2

#Operadores Atribuição:
#num1 += 1 (num1 = num1 + 1)
#num1 -= 1 (num1 = num1 - 1)
#num1 *= 1 (num1 = num1 * 1)
#num1 /= 1 (num1 = num1 / 1)

print("\nOperadores Aritméticos")
print(
    f"a soma de {num1} + {num2} = {soma}"
    f"\na subtração de {num1} - {num2} = {subtracao}"
    f"\na divisão de {num1} / {num2} = {divisao}"
    f"\na multiplicação de {num1} * {num2} = {multiplicacao}"
    f"\no resto da divisão de {num1} % {num2} = {modulus}"
    f"\na potência de {num1} ** {num2} = {potencia}"
)

print("\nOperadores Comparação")
print(
    f"{num1} maior que {num2} = {maior}"
    f"\n{num1} menor que {num2} = {menor}"
    f"\n{num1} maior ou igual que {num2} = {maiorIgual}"
    f"\n{num1} menor ou igual que {num2} = {menorIgual}"
    f"\n{num1} igual que {num2} = {igual}"
    f"\n{num1} diferente que {num2} = {diferente}"
)

print("\nOperadores Atribuição")
print(f"{num1} + 1 = ", num1 + 1)
num1 += 1
print(f"{num1} - 1 = ", num1 - 1)
num1 -= 1
print(f"{num1} * 2 = ", num1 * 2)
num1 *= 2
print(f"{num1} / 2 = ", num1 / 2)
num1 /= 2
print(f"final = {num1}")
