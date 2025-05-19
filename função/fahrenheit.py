def kelvin (celsius):
    kelvin = celsius + 273
    return kelvin

def fahrenheit (celsius):
    fahrenheit = celsius*1.8+32
    return fahrenheit

celsius=int(input("Digite os graus celsius"))
print("a temperatura em kelvin é", kelvin(celsius))
print("a temperatura em fahrenheit é", fahrenheit(celsius))

    