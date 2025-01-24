name = input("nome do filme: ")
releaseYear = int(input("ano de lançamento: "))
movieRating = float(input('nota do filme: '))
includedPlan = input("incluído no plano (s/n)? ") == 's'

# apenas string pode ser concatenados usando o +, para outros tipos devemos usar o (,);
# alternativa 1: prints separados, neste modo não precisa quebrar a linha, a cada novo print a linha é quebrada.
print("\nline print")
print("name: ", name)
print("releaseYear: ", releaseYear)
print("movieRating: ", movieRating)
print("includedPlan: ", includedPlan)

# alternativa 2: bulk print, precisamos quebrar a linha
print("\nbulk print")
print("name: ", name, 
      "\nreleaseYear: ", releaseYear, 
      "\nmovieRating: ", movieRating, 
      "\nincludedPlan: ", includedPlan)

# alternativa 3: com fstring, precisamos quebrar a linha
print("\nfstring print mesma linha")
print(f"name: {name} \nreleaseYear: {releaseYear} \nmovieRating: {movieRating} \nincludedPlan: {includedPlan}")
print("\nfstring print multiplas linhas")
print(f"name: {name}"
      f"\nreleaseYear: {releaseYear}"
      f"\nmovieRating: {movieRating}"
      f"\nincludedPlan: {includedPlan}")

