def cadastro(livros):
    isbn= int(input("digite o codigo do livro"))
    titulo= input("digite o titulo do livro que você deseja")
    autor= input("digite o autor do livro")
    categoria= input("digite a categoria do livro")
    ano_de_publicacao= int(input("digite o ano de publicação"))
    livro={
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano de publicacao": ano_de_publicacao,
            }
    livros.append(livro)


livros=[]

print("")
print("Menu")
print("")
print("digite 0 para sair")
print("Digite 1 para cadastrar os livros")
print("digite 2 para exibir os livros cadastrados")
print("digite 3 para saber a quantidade de livros cadastrados")
print("digite 4 para a lista de títulos")
print("")

while True:
    escolha=int(input("digite sua escolha"))
    if escolha==0:
        print("você saiu")
        break
    elif escolha==1:
        cadastro(livros)
        print("você cadastrou  seu livro")
    elif escolha==2:
        for livro in livros:
            for chave, valor in livro.items():
                print(f"{chave} - {valor}")
    elif escolha==3:
        print(len(livros))
    elif escolha==4:
        for livro in livros:
            print(livros[1])

    
    
    
    
    
    
    
    
    
    
    