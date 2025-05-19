print("numeros pares")

inicio = int(input("Digite um numero"))

n = 0 
quant = 0

while n < inicio:
    n = n + 1
    if n % 2 == 0:
        print(n)
        quant += 1
print("A quantidade de numeros pares é", quant)
    