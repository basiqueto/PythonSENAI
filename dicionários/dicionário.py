
#-------- Dicionário --------

#criar
aluno= {
    "nome": "Vitória",
    "idade": 17,
    "altura": 1.69,
    "matriculado": True 
}

filme1= {
    "nome": "the batman",
    "protagonista": "batman",
    "direcao": "matt reeves",
    "lancado": True

}

filme2= {
    "nome": "moana - um mar de aventuras",
    "protagonista": "moana",
    "direcao": "john musker e ron clements",
    "lancado": True 
}

filme3={
    "nome": "lilo e stitch",
    "protagonista": "stitch",
    "direcao": "todd cherniawsky",
    "lancado": True 
}
#print(aluno)
      
#adicionnar campo
aluno["peso"] = 49

#print(aluno)

#alterar campo
aluno["idade"] = 18

#print(aluno)

#deletar campo
del aluno ["altura"]

#print(aluno)

#verificar
if "altura" in aluno:
    print("altura existente")
else:
   #print("altura inexistente")
    print("")


#exibir
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
print("")


#exibir uma lista de dicionarios
lista_filme = [filme1, filme2, filme3]

    
    #escolhendo os campos
for filme in lista_filme:
    print(f"{filme['nome']} - {filme['protagonista']} - {filme['direcao']} - {filme['lancado']} ")
print("")


    #exibindo todos
for filme in lista_filme:
    for chave, valor in filme.items():
        print(f"{chave}: {valor}")
    
    
    
    
    