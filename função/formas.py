def areas():
    print("digite 1 para area do circulo")
    print("digite 2 para area do retangulo")
    print("digie 3 para area do quadrado")
    print("digite 4 para area do triangulo equilatero")
    print("digite 5 para area do hexagono")
    
def perimetros():
    print("digite 6 para perimetro do circulo")
    print("digite 7 para perimetro do retangulo")
    print("digite 8 para perimetro do quadrado")
    print("digite 9 para perimetro do triangulo equilatero")
    print("digite 10 para perimetro do hexagono")
     

def circulo(raio):
    area= 3.14*raio**2
    return area
    
def retangulo(base,altura):
    area=base*altura
    return area
    
def quadrado(lado):
    area=lado*lado
    return area

def triangulo_equiatero (lado):
    area= lado**2*1.7/4
    return area

def hexagono (lado):
    area= 6*lado**2*1.7/4
    return area

def circulo2 (raio):
    perimetro= 2*1.7*raio
    return perimetro
    
def retangulo2 (lado):
    perimetro= lado+lado+lado+lado
    return perimetro
    
def quadrado2 (lado):
    perimetro=lado+lado+lado+lado
    return perimetro

def triangulo_equilatero2 (lado):
    perimetro= lado+lado+lado
    return perimetro

def hexagono2 (lado):
    perimetro= lado+lado+lado+lado+lado+lado
    return area

a_p=int(input("Você quer area ou perimetro? Se for area digite 1, se for perimetro digite 2"))

if a_p == 1:
    print("areas")

    areas()
    forma=int(input("digite qual forma você deseja:"))
    if forma == 1:
        raio=int(input("digite o raio do circulo:"))
        print("a area do circulo é", circulo(raio))
    elif forma==2:
         base=int(input("digite a base do retangulo:"))
         altura=int(input("digite a altura do retangulo:"))
         print("a area do retangulo é", retangulo(base,altura))
    elif forma==3:
        lado=int(input("digite o lado do quadrado:"))
        print("a area do quadrado é", quadrado(lado))
    elif forma==4:
        lado=int(input("digite a base do triangulo"))
        altura=int(input("digite a altura do triangulo"))
        print("a area do triangulo é:", triangulo_equilatero(lado))
    elif forma==5:
        lado=int(input("digite o lado do triangulo"))
        print("a area do hexagono é", hexagono(lado))
    else:
        print("opção não identificada, escolha somente as opções exibidas")
else:
    a_p == 2
    print("perimetro")
    
    perimetros()
    forma=int(input("digite qual forma você quer?"))
    if forma==6:
        raio=int(input("digite o raio do circulo"))
        print("o perimetro do circulo é", circulo2(raio))
    elif forma==7:
        lado=int(input("digite o lado do retangulo"))
        print("o perimetro do retangulo é", retangulo2(lado))
    elif forma==8:
        lado=int(input("digite o lado do quadrado"))
        print("o perimetro do quadrado é", quadrado2(lado))
    elif forma==9:
        lado=int(input("digite o lado do triangulo equilatero"))
        print("o perimetro do triangulo equilatero é", triangulo_equilatero2(lado))
    elif forma==10:
        lado=int(input("digite o lado do hexagono"))
        print("o perimetro do hexagono é", hexagono2(lado))
    
        
    
    

    


    
    