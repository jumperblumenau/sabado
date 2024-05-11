'''#função lambda
quadrado = lambda numero: numero ** 2
print(quadrado(6))'''

'''#list comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)'''

'''#lambda true
numero = lambda numero: True if numero % 2 == 0 else False
print(numero(2))'''

'''#list comprehension par
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)'''

'''#função lambda concatenação
palavra = lambda x, y: x + y
print(palavra('Rafaela', ' Reis'))'''

'''#list comprehension combinações 123
numeros = [1, 2, 3]
combinacoes = [(n1, n2) for n1 in numeros for n2 in numeros]
print(combinacoes)'''

'''#função lambda soma
soma = lambda numeros: sum(numeros)
print(soma([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))'''

'''#list comprehension media
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
medias = [sum(sublista) / len(sublista) for sublista in (matriz)]
print(medias)'''

'''#função lambda lista de palavras maiusculas
maiuscula = lambda lista: [palavra.upper() for palavra in lista]
print(maiuscula(["loucura", "na grande", "são paulo"]))'''