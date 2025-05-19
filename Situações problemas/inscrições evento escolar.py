import inputs

print("Menu de opções")
print("")

print("digite 1 para cadastrar os nomes")
print("digite 2 para exibir o total de inscritos")
print("digite 3 para exibir a lista de nomes")
print("digite 4 para permitir a consulta de um nome")
print("digite 5 para sair")

nomes=[]
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
        print("O total de inscritos são:", len(nomes))
        
    elif opcao==3:
        nomes.sort()
        for nome in nomes:
            print(nome)
            
    elif opcao==4:
        nome=input("Digie o nome que quer consultar")
        if nome in nomes:
           vari=input("Nome encontrado, você deseja remove-lo da lista? s/n")
           if vari=="s":
               nomes.remove(nome)
               print("nome removido")   
           elif vari == "n":
               print("o nome permanece na lista")
           else:
              print("opção não encontrada")
              
        else:
            vari1=input("Nome não encontrado, deseja adiciona-lo?")
            if vari1=="s":
                nomes.append(nome)
                print("o nome foi adicionado a lista")
        
            elif vari1=="n":
                print("O nome continua fora da lista")
        
            else:
                print("opção inexistente")
    
    elif opcao==5:
        print("Você saiu")
        break
    
    else:
        print("opção inexistente")
        
