from datetime import datetime

def saudacao (nome):
    hora_atual = datetime.now().hour
    
    if hora_atual >= 0 and hora_atual < 5:
      print("boa madrugada", nome)
    elif hora_atual > 5 and hora_atual <=12:
        print("bom dia", nome)
    elif hora_atual > 12 and hora_atual <= 19:
        print("boa tarde", nome)
    elif hora_atual > 19 and hora_atual <= 23:
        print("boa noite", nome)

nome = input("Digite seu nome")
saudacao(nome)
        

      