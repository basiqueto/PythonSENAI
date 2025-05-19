import random
print("level up")

while True:
    print("")
    print("Escolha se você deseja jogar ou como jogar")
    print("Digite 0 para aprender a jogar")
    print("Digite 1 para jogar")
    print("Digite 2 para sair")
    escolha=int(input("Digite sua escolha"))
    
    if escolha==0:
        print("1°-escolha se quer par ou ímpar")
        print("2°-digite o número de 0 a 10")
        print("3°-Descubra se você ganhou")
        print("O jogo funciona da seguinte forma")
        print("Você e eu escolhemos se queremos par ou ímpar, logo após escolhemos 1 número de 0 a 10. Depois disso a soma dos números é afetuada e o resultado definirá quem será o ganhador.")
    elif escolha==1:
        p_i=int(input("Digite 1 para escolher par e 2 para escolher ímpar"))
        n=int(input("escolha um número de 0 a 10"))
        n2=random.randint(1,10)
        soma=n+n2
        print("")
        print("Eu escolhi o número:", n2)
        print("Você escolheu:", n)
        print("")
        if p_i==1 and soma % 2==0:
            print(soma, "a soma é par, você ganhou!!!")
        elif p_i==1 and soma % 2==1:
            print(soma, "a soma é ímpar, você perdeu!")
        elif p_i==2 and soma % 2 ==0:
            print(soma, "a soma é par, você perdeu!")
        else:
            print(soma, "a soma é ímpar você ganhou!")
            
    elif escolha==2:
        print("Você saiu!")
        break
     
    else:
        print("opção não identificada")