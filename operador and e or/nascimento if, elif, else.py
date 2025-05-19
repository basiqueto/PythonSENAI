print("ano de nascimento")

nasci= int(input("digite seu ano de nascimento"))
ano_atual= 2025

if ano_atual <= 2025 and ano_atual >=  1908 and nasci >= 1908 and nasci <= 2025: 

    idade= ano_atual - nasci 

    if idade <= 10:
        print(idade, "você é uma criança")
        
    elif idade >= 11 and idade <= 17:
        print(idade, "você é um adolescente")
        
    elif idade >= 18 and idade <= 59:
        print(idade, "você é um adulto")
        
    elif idade >= 60:
        print(idade, "você é um idoso")

else:
    print("ano inválido")
