lista =[

{
'nome' : 'Joao',
'idade' : '19'

}


]

def cadastro(nome, idade, lista):
    lista.append({'nome' : nome, 'idade' : idade})

while True:
    esc = input('1-Cadastrar cliente\n2-Buscar cliente\n3-Deletar\n4-Sair')

    if esc == 'Cadastrar' or 'cadastrar':
        cadastro(input('Nome: '), input('Idade: '), lista)


    if esc == 'Sair' or 'sair':
        break