imposto=0.3

#Criando uma funcao "normal
def preco_imposto(preco):
    return preco*(1+0.3)
print(preco_imposto(100))

#Criando uma funcao lambda
preco_imposto2 = lambda preco:preco*(1.0+imposto)
print(preco_imposto2(100))