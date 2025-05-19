#passo a passo

#1 solicite um produto com o preço dele

#2 aplique 5% de desconto

# 3
#passo1: divir 5 por 100
#passo2: multiplicar o resultado pelo valor do produto
#passo3: exibir o valor final e o quanto o valor diminuiu

print("desconto")

nome = input("qual o nome produto")
preço= int(input("digite o preço do produto"))
resultado =  preço/5
resultado2 = preço - resultado

print("o novo preço do produto", nome, "é de", resultado2)
