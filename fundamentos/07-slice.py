"""
    fatiamento de strings (slice)
    podemos definir o fatiamente como uma forma de recuperar partes de uma string
    a string tem o seguinte formato:
    string[indexInicio : indexFim] -> o índice de início é sempre 0, e o fim é o tamanho da String - 1; 
"""
# exemplo abc -> [a = posição 0, b = posição 1, c = posição 2]
print("abc"[0:]) # toda string a partir da primeira posição
print("abc"[:3]) # toda String até a última posição
print("abc"[1:3]) # toda String a partir da segunda posição
print("abc"[0:0]) # retorna vazio
print("abc"[3:0]) # retorna vazio
print("abc"[:]) # toda a string

"""
    fatiamento com passo, terceiro argumento da string
    podemos definir a orientação e a quantidade de caracteres por iteração
    a string com o terceiro argumento:
    string[indexInicio : indexFim : passo] -> o passo por padrão é sempre 1 se não definirmos
"""

print("abcd"[0::2]) # toda string de dois em dois caracteres (índices pares)
print("abcd"[1::2]) # toda string de dois em dois caracteres a partir da segunda posição (índices ímpares)
print("abcd"[::-1]) # retorna a string invertida começando pelo último caractere até o primeiro.
