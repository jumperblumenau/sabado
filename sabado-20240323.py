'''peso1 = float(input("Qual o peso da primeira avaliação?"))
nota1 = float(input("Digite a quanto você tirou na primeira avaliação:"))
peso2 = float(input("Qual o peso da segunda avaliação?"))
nota2 = float(input("Digite a quanto você tirou na segunda avaliação:"))
peso3 = float(input("Qual o peso da terceira avaliação?"))
nota3 = float(input("Digite a quanto você tirou na terceira avaliação:"))

media_p = (peso1*nota1 + peso2*nota2 + peso3*nota3)/(peso1 + peso2 + peso3)
print(f'você tirou {media_p},parabéns')'''


#n1 = float(input('digite o primeiro numero'))
#n2 = float(input('digite o primeiro numero'))
#n3 = float(input('digite o primeiro numero'))
#l = [2, 10 ,56, 22, 33, 68, 11, 8, 5, 7]
#print(f'o maior numero dessa lista é {max(l)} eo menor é {min(l)}')

'''from random import

n = randrange(1, 100)
chute = int(input('digite um numero:')
            if chute > n:
                print(f'o numero digitado é mmaior, tentativas restantes: {t}')
            else:
                print(f'o numero digitado é menor, tentativas restantes: {t}')
            if chute == n:
                print(f'você ganhou! o numero era {n}')
            t -= 1
            d = input('você quer desistir? *sim *não:')
            if d == 'sim':
                break
            else:
                print('ok')'''

'''def tabuada(n):
    for i in range (1, 11):
        return (f'{n} x {i} = {n+i}')
    n = int(input('digite um numero'))
    print(tabuada(n)'''

'''def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def circulo(r):
    return (r**2) * 3,14

print(f'''
    #escolha entre calcular a area de :
    #1.quadrado
    #2.retangulo
    #3.circulo
''')
n = input('digite a sua opção:')
if n =='1':
    l = float(input('digite o lado do qudrado'))
print(quadrado(l))
elif n == '2':
    b = float(input('digite a base do retangulo:'))
    h = float(input('digite a altura do retangulo:'))
    print(f'a area ')'''

l = []
for i in range (10):
    n1 = input('digite as notas:')
    l.append(n1)