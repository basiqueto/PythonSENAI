def imc (peso,altura):
    imc=peso/(altura*altura)
    return imc

def imc2 (_imc):
    if _imc <= 18.5:
        print("Você está abaixo do peso")
    elif _imc >18.5 and _imc <=24.9:
        print("Você está normal")
    elif _imc > 25 and _imc <=29.9:
        print("Você está sobrepeso")
    elif _imc > 30 and _imc <= 34.9:
        print("Você está classificado em obesidade grau 1")
    elif _imc >30 and _imc <=39.9:
        print("Você está classificado em obesidade grau 2")
    else:
        _imc > 40
        print("Você está classificado em obesidade grau 3")
        
altura=float(input("Digite sua altura em metros"))
peso=float(input("Digite seu peso em Kg"))
_imc= imc(peso,altura)

imc2(_imc)