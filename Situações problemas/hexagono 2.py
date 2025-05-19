#passo a passo

#1 achar area do hexagono
#2 dividir o hexagono em seis triângulos
#3 solicitar a medida do lado do hexagono
#4 elevar a medida do lado do triângulo ao quadrado
#5 descobrir raiz de 3
#6 multiplicar a raiz pela potenciação da medida do lado 
#7 dividir por 4
#8 multiplicar tudo por 6

print("area hexagono")
lado = int(input("digite a medida do lado dos triângulos:"))
lado2 = lado * lado
raiz = round(3 ** 0.5, 2)
multiplicacao = lado2 * raiz
divisao = multiplicacao / 4
multiplicacao2 = round(divisao * 6, 2)

print("a area do hexagono é igual a", multiplicacao2)