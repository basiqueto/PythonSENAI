import inputs

print("Menu de opções")
print("")

print("digite 1 para cadastrar os nomes")
print("digite 2 para exibir o total de pais")
print("digite 3 para exibir a lista de nomes")
print("digite 4 para a confirmação de presença")
print("digite 5 para exibir o relatório da chamada")
print("digite 6 para sair")

nomes=[]
presentes=[]
ausentes=[]
while True:
    opcao=inputs.input_int("Digite sua escolha")
    print("")


    if opcao==1:
        nome=input("digite o nome que deseja cadastrar")
        if nome in nomes:
            print("Nome ja cadastrado")
        else:
            nomes.append(nome)
            print("Nome cadastrado com sucesso")
    
    elif opcao==2:
        print("O total de pais são:", len(nomes))
        
    elif opcao==3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    elif opcao==4:
       nome=input("Digite um nome para verificar se está presente:")
       if nome in nomes:
           presentes.append(nome)
           print("nome está em nossa lista de presentes")
       else:
           ausentes.append(nome)
           print("nome está em nossa lista de ausentes")
    
    elif opcao==5:
        print("lista de presentes:")
        for item in presentes:
            print(item)
        print("")
        print("lista de ausentes:")
        for item in ausentes:
            print(item)
        
    elif opcao==6:
        print("Você saiu")
        break
    
    else:
        print("opção inexistente")
        
