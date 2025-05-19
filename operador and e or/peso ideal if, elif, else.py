print("IMC")

altura= float(input("digite sua altura em metros"))
peso= float(input("digite seu peso em kg"))

IMC= peso/altura**2

if IMC < 19.1:
    print(f'{IMC:.2f}, "voce esta abaixo do peso"')
elif IMC > 19.1 and IMC <= 27.3:
    print(f'{IMC:.2f}, "voce esta no peso ideal"')
elif IMC > 27.3 and  IMC <= 32.3:
    print(f'{IMC:.2f}, "voce esta acima do peso"')
elif IMC > 32.4:
    print(f'{IMC:.2f}, "voce esta obeso"')