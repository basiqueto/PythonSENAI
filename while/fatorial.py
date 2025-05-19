while True:
    print("Qual das opções de operações você deseja?")
    print("0-sair")
    print("1-fatorar")
    print("2-quadrado")
    print("3-cubo")
    print("4-tabuada")
    
    
    menu = int(input("digite qual operação você deseja"))
    if menu != 0:
        n = int(input("digite o número que você quer fazer a operação "))
    if menu == 0:
        print("você escolheu sair")
        break
    elif menu == 1:
        contador = 1
        fator = contador
        while n > contador:
            fator = fator * (contador+1)
            contador = contador + 1
        print(contador)
        print(fator)
    elif menu == 2:
        print(n**2)
    elif menu == 3:
        print(n**3)
    elif menu == 4:
        print(n*1)
        print(n*2)
        print(n*3)
        print(n*4)
        print(n*5)
        print(n*6)
        print(n*7)
        print(n*8)
        print(n*9)
        print(n*10)
    else:
        print("opção invalida")