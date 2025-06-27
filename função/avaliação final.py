def exibir ():
    print("Cadastro para a média ")
    print("digite 1 para cadastrar suas 3 notas e descobrir a média ")
    print("Digite 2 para cadastrar o nome do aluno ")
    print("Digite 3 para exibir o resumo final")
    print("Digite 0 para sair ")
    
def calcular_media(n1, n2, n3):
    media= (n1+n2+n3)/3
    return media

def verificar_situacao(media):
    if calcular_media(n1, n2, n3) >= 7:
        print("sua media é:", calcular_media(n1, n2, n3), "esta aprovado!")
    elif calcular_media(n1, n2, n3) >= 5 and calcular_media(n1, n2, n3) < 7:
        print("sua media é:", calcular_media(n1, n2, n3), "está de recuperação :(")
    elif calcular_media(n1, n2, n3) <5:
        print("sua média é:", calcular_media(n1, n2, n3), "está reprovado :(")
        
def cadastrar_aluno(alunos):
    nome=input("Digite o nome do aluno ")
    media=float(input("Digite a média do aluno "))
    situacao=input("Digite a situacão do aluno")
    aluno={
        "nome": nome,
        "média": media,
        "situação": situacao,
}
    alunos.append(aluno)
    
def mostrar_relatorio(alunos):
     for aluno in alunos:
            for chave, valor in aluno.items():
                print(f"{chave} - {valor}")
    
alunos=[]



while True:
    exibir()
    escolha=int(input("digite sua escolha "))
    if escolha == 0:
        print("você saiu")
        break
    elif escolha == 2:
        cadastrar_aluno(alunos)
    elif escolha == 1:
        n1=float(input("digite sua primeira nota "))
        n2=float(input("digite sua segunda nota "))
        n3=float(input("digite sua terceira nota"))
        verificar_situacao(calcular_media(n1, n2, n3))
    elif escolha==3:
        mostrar_relatorio(alunos)
    else:
        print("escolha invalida")
        


    
    