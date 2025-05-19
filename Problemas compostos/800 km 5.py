#passo a passo

#1 quantos litros de combustivel e quantos reais é preciso para fazer uma viagem de 800 km sendo que o carro tem uma autonomia de 7 km por litro
#2 autonomia do carro, a distancia total da viagem e o valor do litro do combustivel

# 3
#passo 1: subtrair a distancia total a ser percorrida (800) por quanto ja percorreu (90)
#passo 2: pegar o resultado e dividir pela autonomia do carro (7)
#passo 3: subtrair o resultado da divisão por quantos litros ainda tem no carro (10)
#passo 4: pegar o resultado e multiplicar pelo valor do combustivel
#passo 5: exibir o total de litros e o valor necessario

print("800 quilometros")

subtração = 800-90
divisão = subtração/7
sub2 = divisão-10
multiplicação = sub2 * 6.90

print("o total de litros necessarios é de ", divisão)
print("o valor necessario é de ", multiplicação, "reais")