def input_str(recado):
    while True:
        nome=input(recado)
        
        if not nome.isalpha():
            print("Erro, digite apenas letras")
            
        else:
            return nome
    
def input_int(recado):
    while True:
        try:
            numero = int(input(recado))
            return numero
        except ValueError:
            print("Erro, digite apenas números inteiros")
            
def input_float(recado):
    while True:
        try:
            num= float(input(recado))
            return num
        except ValueError:
            print("Erro, digite apenas números")
            
            
print(input_str("Digite um nome"))

            
        
        
    
