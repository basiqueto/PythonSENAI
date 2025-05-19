import inputs
def exibir():
    print("menu da calculadora")
    print("1- soma")
    print("2- subtracao")
    print("3- multiplicacao")
    print("4- divisao")

def soma (num1, num2):
    return num1+num2
def subtracao (num1, num2):
    return num1-num2
def multiplicacao (num1,num2):
    return num1*num2
def divisao (num1,num2):
    return num1/num2

def calculos(num1, num2):
    print("o resultado da soma é", soma(num1,num2))
    print("o resultado da subtracao é", subtracao(num1,num2))
    print("o resultado da multiplicacao é", multiplicacao(num1,num2))
    print("o resultado da divisao é", divisao(num1,num2))
    
def calculo(num1, num2, calculos):
    if calculos== 1:
        print("o resultado da soma é",soma(num1,num2))
    elif calculos==2:
        print("o resultado da subtração é", subtracao(num1,num2))
    elif calculos==3:
        print("o resultado da multiplicação é", multiplicacao(num1,num2))
    elif calculos==4:
        print("o resultado da divisao é", divisao(num1,num2))

exibir()
while True:
    try: 
        operacoes= inputs.input_int("Digite qual operação você quer:")
        break
    except ValueError:
        print("Digite apenas números")
        
while True:
    try:
        num1= inputs.input_int("digite o primeiro numero")
        break
    except ValueError:
        print("Digite apenas números")
        
while True:
    try:
        num2= inputs.input_int("digite o segundo numero")
        break
    except ValueError:
        print("Digite apenas números")
calculo(num1, num2, operacoes)

print(inputs.input_int("Digite qual operação você quer"))


