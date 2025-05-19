#etapa 1-Criar uma lista com 5 itens
objetos= ["mesa", "ventilador", "caneta", "cadeira", "garrafa"]
print("lista de objetos criada")

#etapa-2 adicionar mais um objeto 
objetos.append("ar-condicionado")
print("objeto adicionado")

#etapa-3 acessar o objeto que está na segunda posição e exibir
print(objetos[1])
print("objeto na segunda posição acessado")

#etapa-4 remover um objeto da lista
removidos= objetos.pop(2)
print(removidos)
print("objeto removido")
print("")

#etapa-5 exibir o tamanho da lista
print(len(objetos))
print("tamanho da lista exibido")
print("")

#etapa-6 mostrar todos os itens da lista
for objeto in objetos:
    print(objeto)
#etapa-7 verificar se a cadeira está na lista
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("cadeira removida")
else:
    objetos.append("cadeira")
    print("cadeira adicionada")

#etapa-8 ordenar a lista em ordem alfabética
print(objetos)
objetos.sort()
print("lista organizada em ordem alfabética")

print(objetos)

#etapa-9 exibir o primeiro objeto
print(objetos)
objetos.append(0)
print("primeiro objeto exibido")

#etapa-9 exibir o ultimo objeto
ultimo = objetos.pop()
objetos.append(ultimo)
print(ultimo)
print("ultimo objeto exibido")

#etapa-10 limpar toda a lista
objetos.clear()
print("lista limpa")