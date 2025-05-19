print("triangulo")

lado1 = int(input("qual é o primeiro lado?"))
lado2 = int(input("qual é o segundo lado?"))
lado3 = int(input("qual é o segundo lado?"))

if lado1==lado2 and lado2==lado3 and lado1==lado3:
    print("o triangulo é equilatero")
elif lado1==lado2 and lado2 == lado3 and lado2 != lado3 or lado1 == lado2 and lado2 != lado3 and lado1 == lado3 or lado1 != lado2 and lado2 == lado3 and lado1 == lado3 or lado1 != lado2 and lado2 != lado3 and lado1 == lado3 or lado1 == lado2 and lado2 != lado3 and lado1 != lado3 or lado1 != lado2 and lado2 == lado3 and lado1 != lado3:
    print("o triangulo é isosceles")
else:
    print("o triangulo é escaleno")
