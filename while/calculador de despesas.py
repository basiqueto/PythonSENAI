
valor = 0
n_despesas= 0

while True:
    print("Calculdor da despesas")
    print("1-Adicionar valor da despesa")
    print("2-Mostrar a quantidade e o valor total das despesas")
    print("0-Sair")
    menu = int(input("Qual das opções deseja?"))
    
    if menu == 0:
        print("Você saiu!")
        break
    elif menu == 1:
        adc_valor = int(input("Adicione um valor que deseja"))
        print("Você adicionou", adc_valor, "reais")
        n_despesas += 1
        valor = adc_valor + valor
        
    elif menu == 2:
        print("O total de despesas que você tem é", n_despesas, "que somam" , valor, "reais")
        
    else:
        print("opção não identificada")

    