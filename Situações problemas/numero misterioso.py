import random
print("Você está dentro do jogo de adivinhação")
def mist():
    n2=random.randint(0,100)
    return n2 

misterio=mist()

while True:
    n_misterioso=int(input("Digite o número que você acha que eu escolhi, lembrando que é de 0 a 100"))
    print("")
    if n_misterioso==misterio:
        print("Você ganhou!")
        print("Digite 1 para jogar mais uma")
        print("Digite 2 para sair do jogo")
        print("")
        escolha=int(input("Me fale sua escolha"))
        if escolha==1:
            misterio=mist()
        elif escolha==2:
            print("Você saiu!!")
            break
    elif n_misterioso<misterio:
        print("o número que você escolheu é menor que o meu")
    elif n_misterioso>misterio:
        print("o número que você escolheu é maior que o meu")
            

        
        
  