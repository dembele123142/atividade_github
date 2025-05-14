lista =[

{
'nome' : 'Joao',
'idade' : '19'

}


]
true_while = True

def buscar_cliente(nome,lista):
    for dicionario in lista:

        if dicionario['nome'] == nome:
            print('Existe.')
        else:
            print('Não existe.')

def cadastro(nome, idade, lista):
    lista.append({'nome' : nome, 'idade' : idade})

while true_while:
    esc = input('1-Cadastrar cliente\n2-Buscar cliente\n3-Deletar\n4-Sair: ')

    if esc == '1':
        nome = input('Nome: ')
        idade = input('Idade: ')
        cadastro(nome, idade, lista)
        print(lista)
        print('')




    if esc == '2':
        quem = input('Quem buscar?: ')
        buscar_cliente(nome=quem, lista=lista)
        print('')



    if esc == '4':
        true_while = False
        