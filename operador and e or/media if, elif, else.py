print("média")

nt1=int(input("digite sua primeira nota"))
nt2=int(input("digite sua segunda nota"))

if nt1 > 0 and nt1 <= 100 and nt2 > 0 and nt2 <= 100:
    

    adicao= nt1+nt2
    nota= adicao/2

    if nota >= 70:
        print(nota, "você está aprovado")
    elif nota >= 50 and nota < 70:
        print(nota, "você está de recuperaçao")
    elif nota <50:
        print(nota, "você foi reprovado")

else:
    print("sua nota é inválida")
