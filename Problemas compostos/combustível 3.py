#passo a passo

#1 quanto custa encher o tanque do carro

#2 capacidade do combustivel do carro em litros. Quantos litros o carro ja tem? E o valor do litro do combustiel em reais

# 3
#passo 1: subtrair a capacidade total (50) e o quanto o tanque do carro ja esta cheio (20)
#passo 2: multiplicar o resultado da subtração pelo preço do combustivel
#passo 3: exibir o custo

print("tanque do carro")

capacidade = 50 - 20
multiplicar = capacidade * 5.80

print("o custo total é de ", multiplicar, "reais")

#passo a passo

#1 quanto custa encher o tanque do carro

#2 capacidade do combustivel do carro em litros. Quantos litros o carro ja tem? E o valor do litro do combustiel em reais

# 3
#passo 1: subtrair a capacidade total (50) e o quanto o tanque do carro ja esta cheio (20)
#passo 2: multiplicar o resultado da subtração pelo preço do combustivel
#passo 3: exibir o custo

print("tanque do carro")

tanque = int(input("digite a capacidade do tanque"))
cheio = int(input("digite o quanto o tanque ja esta cheio"))
capacidade = tanque - cheio
valor = float(input("digite o preço do litro de combustivel"))
multiplicar = capacidade * valor

print("o custo total é de ", multiplicar, "reais")

