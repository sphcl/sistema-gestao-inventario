#Aqui está espaço para o trecho de código do login e autenticação com o arquivo login.txt
#Após essa etapa o usuário é levado para o menu de operações

def menu():
    """Função que organiza as outras funções do código em um
    menu de operações. O usuário executa apenas as funções que
    escolher de acordo com o menu"""

    #Exibe as ações que o usuário pode ter no nosso programa
    while True:
        print('====== Menu de Operações: ======')
        print('1. Redefinir Login e senha')
        print('2. Adicionar produto')
        print('3. Remover produto')
        print('4. Atualizar produto')
        print('5. Exibir lista de produtos')
        print('6. Encontrar produto')
        print('7. Estatísticas do inventário')
        print('8. Sair do menu de operações')
    
        #Solicita ao usuário uma decisao
        decisao = int(input('Escolha uma opção do menu de operações: '))

        if decisao == 1:
            redefinir_senha()
        elif decisao == 2:
            adiciona_item(produtos)
        elif decisao == 3:
            remove_item(produtos)
        elif decisao == 4:
            atualiza_item(produtos)
        elif decisao == 5:
            exibe_iventario(produtos)
        elif decisao == 6:
            encontra_item(produtos)
        elif decisao == 7:
            estatistica_inventario(produtos)
        elif decisao == 8:
            break
        else:
            print('Essa opção não existe. Tente novamente')


#Função vazia por enquanto
def redefinir_senha():
    pass

#Lembrar de editar a função para incluir a cifra de cesar que
# vai codificar o preço e a quantidade de todos produtos que forem
# adicionados ao inventário

def adiciona_item(produtos):
    """Fução para adicionar um novo item (chave:valor)
     ao dicionário produtos"""

    chave = input('Insira o ID do produto: ')

    nome = input('Insira o nome do produto: ')
    qtd = int(input('Insira quantidade de unidades do produto: '))
    preco = float(input('Insira o preço do produto (uma casa depois do ponto): '))
    importado = input('O produto é importado? s/n: ')

    if importado == 's':
        importado = True
    else: 
        importado = False

    valor = [nome, qtd, preco, importado]

    produtos[chave] = valor

    #mostrando para o usuário o nome do produto que ele adicionou ao inventário
    print(f'{valor[0]} adicionado com sucesso ao inventário de produtos')

    #Devolvendo o usuário ao menu de operação
    menu()

#Função vazia por enquanto -  lelet e jaja
def remove_item(produtos):
    pass

#Função vazia por enquanto -  lelet e jaja
def atualiza_item(produtos):
    pass

#Função vazia por enquanto
def exibe_iventario(produtos):
    pass

#Função vazia por enquanto
def encontra_item(produtos):
    pass

#Função vazia por enquanto
def estatistica_inventario(produtos):
    pass

# Criando inventario Produtos
produtos = {}

#chamando a função menu para começar o programa
menu()
aaaaaaaaaaaa
#exibindo o inventário
# print(produtos)
