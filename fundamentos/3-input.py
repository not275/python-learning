"""input função de entrada
   o input recebe apenas valores do tipo string por padrão;
   para mudar o tipo precisamos converter fazendo um cast do tipo
   obs: \n quebra de linha
"""

name = input("nome do filme: ")
releaseYear = int(input("ano de lançamento: "))
movieRating = float(input('nota do filme: '))
# podemos verificar um boleano comparando uma string, se o valor for igual é true, se não false;
includedPlan = input("incluído no plano (s/n)? ") == 's'

print(name)
print(releaseYear)
print(movieRating)
print(includedPlan)

print("\ntipos:")
print(type(name))
print(type(releaseYear))
print(type(movieRating))
print(type(includedPlan))