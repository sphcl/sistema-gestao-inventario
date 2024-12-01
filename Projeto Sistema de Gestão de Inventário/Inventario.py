import hashlib
def crialogin(): 
    """Função que começa o login do usuário. Cria ou apenas lê um arquivo 'login.txt' ja existente """
    try: #tenta abrir o arquvo 'logn.txt para ler (se existir)
        a = open('login.txt', 'r')
        autentica() #Chama a função 'autentica', porque se no arquivo 'login.txt' ja tiver algum conteúdo
                     #a entrada do usuário precisa ser autenticada
    except FileNotFoundError:
        a = open('login.txt', 'w+') #Caso não exista um arquivo 'login.txt' ele cria e permite a escrita
        usuario = input('Cadastre o nome do usuário:')
        usuario = hashlib.sha256(usuario.encode()).hexdigest() #Aplicando a função hash236 para o nome do usuario
        senha = input('Cadastre a senha:')
        senha = hashlib.sha256(senha.encode()).hexdigest() #Aplicando a função hash236 para a senha do usuario
        a.write(f'{usuario}\n{senha}\n')
        menu() #Chama a função menu. Ja que é o primeiro cadastro do usuário ele não precisa ser autenticado

def autentica(): 
    """Função que autentica o login do usuário caso o arquivo login.txt ja exista no momento que ele roda programa"""
    #Se o arquivo login.txt ja tem conteúdo, pede ao usuario as informações de entrada para autenticação
    #função hash sempre resulta no mesmo valor para um conteúdo específico, assim conseguimos validar as entradas com o que está no arquivo
    usuarioinput = input('Digite o nome do usuário:')
    usuarioinput = hashlib.sha256(usuarioinput.encode()).hexdigest() #criptografa entrada usuario
    senhainput = input('Digite a senha:')
    senhainput = hashlib.sha256(senhainput.encode()).hexdigest() #criptografa entrada senha 

    try: 
        with open('login.txt', 'r') as a: #abre o arquivo apenas para leitura
            usuario = a.readline().strip() #lê a primeira linha criptografada do arquivo e atribui a variável 'usuário'
            senha = a.readline().strip() #lê a segunda linha criptografada do arquivo e atribui a variável 'senha'

            autenticacao = usuarioinput == usuario and senhainput == senha #variavel 'autenticacao' vai receber a comparaçao das entradas 'usuarioinput' e 'senhainput'
                                                                           # com o usurio e senha que ja estavam no arquivo 'login.txt', através da hash256
                                                                           # ela retorna true ou false internamente
            if autenticacao: #Se a variável autenticacao for verdadeira, ou seja, login autenticado
                print('Autenticação bem-sucedida')
                menu() #Como o login foi autenticado, encamiinhamos o usuario para a função menu() para ele seguir no fluxo do programa
            else:
                print('Usuario ou senha incorretos. Tente novamente') #caso a autenticação não seja bem sucedida
                autentica() # chama a função autentica para o usuério tentar novamente colocar as informações corretas
    
    except FileNotFoundError:
            print('Login não identificado.')
            return False, None

def menu():
    """Função que organiza as outras funções do código em um menu de operações. O usuário executa apenas as funções que
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
            exibe_inventario(produtos)
        elif decisao == 6:
            encontra_item(produtos)
        elif decisao == 7:
            estatistica_inventario(produtos)
        elif decisao == 8:
            break
        else:
            print('Essa opção não existe. Tente novamente')
            
def redefinir_senha():
    """Função que leva o usuário para outra autenticação para coseguir redefinir a senha"""
    print("Para redefinir a senha, autentique-se primeiro.")
    autentica2()  # Reutilizando a função de autenticação

def autentica2(): 
    """Função que autentica o login do usuário com o conteúdo do arquivo login.txt e o encaminha para alterar a senha"""
    #função igual 'autentica()' mas apenas para a autentficação de redefir senha. Porque a outra função de autenticação leva o usuário para a função menu(), 
    # essa vai levar o usuário para a função senha_nova()
    usuario2 = input('Digite o nome de usuário atual:')
    usuario2 = hashlib.sha256(usuario2.encode()).hexdigest()
    senha2 = input('Digite a senha atual:')
    senha2 = hashlib.sha256(senha2.encode()).hexdigest()
    
    try: 
        with open('login.txt', 'r') as a:
            usuario = a.readline().strip() #lê a primeira linha
            senha = a.readline().strip() #lê a segunda linha

            autenticacao = usuario2 == usuario and senha2 == senha #compara a original com a inserida
            if autenticacao: #Se a variável autenticado for verdadeira
                print('Autenticação bem-sucedida')
                senha_nova() #após autenticação bem sucedida o usuário pode definir uma senha nova
            else:
                print('Usuario ou senha incorretos. Tente novamente')
                autentica2() # chama a função autentica2 para o usuário tentar novamente colocar as informações corretas     

    except FileNotFoundError: #caso não exista o primeiro acesso
            print('Login não identificado. Crie um login primeiro')

def senha_nova():
    """Função que permite o usuário redefinir a sua senha e atualiza as novas informações no arquivo login.txt"""
    nova_senha = input('Digite a nova senha: ').strip() #usuário escreve a nova senha que ele deseja
    nova_senha_confirmacao = input('Confirme a nova senha: ').strip() # confrma a nova senha que ele quer

    if nova_senha == nova_senha_confirmacao: #Valida se o usuáro escreveu a senha corretamente
            usuario = input('Insira o nome do usuário atual: ') #pede o nome do usuário só para conseguir escrever no 'login.txt' de novo
            usuario = hashlib.sha256(usuario.encode()).hexdigest() #crptografar o usuário de novo para conseguir validar a entrada depois da redefinção da senha 
            nova_senha = hashlib.sha256(nova_senha.encode()).hexdigest() # crptografa a nova senha
            with open('login.txt', 'w') as a:
                a.write(f'{usuario}\n{nova_senha}\n') #apaga tudo que tem no arquivo 'logn.txt' e escreve o usuário e a nova senha definidos nessa função 
            print("Senha redefinida com sucesso!")
        
    else: #caso o usuáro tenha escrito a nova senha e a confirmação de formas diferentes, ele precisa fazer de novo
            print("As senhas não correspondem. Tente novamente.")
            nova_senha()

def cesar(texto, chave=2): #recebe o preço e o valor dos produtos do inventário como uma string
    L = list(texto) #transforma string em uma lista
    for i in range(len(L)):
        L[i] = proximo(L[i], chave)
    return ''.join(L)

def proximo(letra, chave=2):
    return chr(ord(letra) + chave) #transforma a letra em número e depos em string de novo

def adiciona_item(produtos):
    """Função que adiciona um novo item (chave:valor) com as informações de 'id', 'nome', 'quantidade', 'preço' e se é 'importado' ao inventário produtos"""

    chave = input('Insira o ID do produto: ')

    nome = input('Insira o nome do produto: ')
    qtd = int(input('Insira quantidade de unidades do produto: '))
    preco = float(input('Insira o preço do produto (uma casa depois do ponto): '))
    importado = input('O produto é importado? s/n: ')

    if importado == 's':
        importado = True
    else: 
        importado = False

    valor = {
        'nome': nome, 
        'qtd': cesar(str(qtd)), 
        'preco': cesar(str(preco)), 
        'importado': importado
        }

    produtos[chave] = valor

    #mostrando para o usuário o nome do produto que ele adicionou ao inventário
    print(50 * '-')
    print(f'{valor["nome"]} adicionado com sucesso ao inventário de produtos')
    print(50 * '-')

    #Devolvendo o usuário ao menu de operação
    menu()

def remove_item(produtos):
    """Função para remover um item do dicionário de produtos"""
    
    chave = input('Insira o ID do produto que deseja remover: ')
    
    if chave in produtos:
        del produtos[chave] #função que remove um item do dicionário
        print(50 * '-') #mostrando para o usuério que o item foi removido
        print(f'Produto com ID {chave} removido com sucesso do inventário.')
        print(50 * '-')
    else:
        print(50 * '-') #mostrando para o usuário que o item não existe no iventário
        print(f'O produto com ID {chave} não existe no inventário.')
        print(50 * '-')

    # Devolvendo o usuário ao menu de operação
    menu()

def atualiza_item(produtos):
    """Função que permite atualizar informações de um produto existente no inventário."""
    if not produtos:
        print("O inventário está vazio. Nenhum produto para atualizar.")
        menu()
        return

    #solicita o ID do produto a ser atualizado
    chave = input('Digite o ID do produto que deseja atualizar: ').strip()

    if chave not in produtos:
        print(50 * '-')
        print(f'O produto com ID {chave} não foi encontrado no inventário.')
        print(50 * '-')
        menu()
        return

    #exibir as informações atuais do produto
    produto = produtos[chave]
    print(50 * '-')
    print(f"ID: {chave}")
    print(f"Nome: {produto['nome']}")
    print(f"Quantidade: {cesar(produto['qtd'], decrypt=True)}")
    print(f"Preço: {cesar(produto['preco'], decrypt=True):.2f}")
    print(f"Importado: {'Sim' if produto['importado'] else 'Não'}")
    print(50 * '-')

    #solicitar ao usuário os campos que ele deseja atualizar
    print("Quais informações você deseja atualizar?")
    print("1. Nome")
    print("2. Quantidade")
    print("3. Preço")
    print("4. Importado")
    print("5. Voltar ao menu")
    opcao = int(input("Digite o número da opção desejada: ").strip())

    if opcao == 1:
        produto['nome'] = input('Digite o novo nome do produto: ').strip()
    elif opcao == 2:
        produto['qtd'] = int(input('Digite a nova quantidade do produto: ').strip())
    elif opcao == 3:
        produto['preco'] = float(input('Digite o novo preço do produto: ').strip())
    elif opcao == 4:
        importado = input('O produto é importado? (s/n): ').strip().lower()
        produto['importado'] = True if importado == 's' else False
    elif opcao == 5:
        menu()
        return
    else:
        print("Opção inválida. Tente novamente.")
        atualiza_item(produtos)
        return

    #confirmar a atualização
    print(50 * '-')
    print("Produto atualizado com sucesso!")
    print(f"ID: {chave}")
    print(f"Nome: {produto['nome']}")
    #print(f"Quantidade: {cesar(produto['qtd'])}")
    #print(f"Preço: {cesar(produto['preco']):.2f}")
    print(f"Importado: {'Sim' if produto['importado'] else 'Não'}")
    print(50 * '-')
    
    #voltar ao menu principal
    menu()

#Função em teste ainda - duda
def exibe_inventario(produtos):
    """
    Função para exibir os produtos no inventário em ordem alfabética de nomes.
    """

    #Verifica se o dicionário está vazio
    if not produtos:
        print("O inventário está vazio.")
        return

    #Converte os produtos para uma lista de tuplas (ID, [nome, qtd, preco, importado])
    produtos_lista = [(k, v) for k, v in produtos.items()]

    #Função de bubble sort para ordenar pelo nome
    n = len(produtos_lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if produtos_lista[j][1][0].lower() > produtos_lista[j + 1][1][0].lower():
                produtos_lista[j], produtos_lista[j + 1] = produtos_lista[j + 1], produtos_lista[j]

    #Exibindo os produtos ordenados
    print("Inventário de Produtos (Ordenado por Nome):")
    print("-" * 40)
    for id_produto, dados in produtos_lista:
        nome, qtd, preco, importado = dados
        print(f"ID: {id_produto}")
        print(f"Nome: {nome}")
        print(f"Quantidade: {qtd}")
        print(f"Preço: R${preco:.2f}")
        print(f"Importado: {'Sim' if importado else 'Não'}")
        print("-" * 40)


#esse encontra item tem q verificar a existência de um produto (por ID ou nome).
def encontra_item(produtos):
    proc_prod = int(input('Digite 1 para uma busca detalhada ou 2 para verificar apenas a existência do produto:'))

    if proc_prod == 1:
        
        busca = input("Você quer buscar um item pelo seu nome ou pelo ID? (Digite 'nome' ou 'id'): ").strip().lower() #o usuário insere sua opção e independete de como estiver escrito
                                                                                                                      #vai ser convertido em letras maiúsculas e sem espaços
        if busca == 'nome':  #se o usuário preferiu a busca por nome
            busca_nome = input('Digite o nome do item, por favor: ').strip().lower()
            encontrado = False

            for chave, valor in produtos.items(): 
                ID = chave
                valor['nome']

            # Procurando pelos itens para verificar correspondência de nomes
            for produto in produtos.values():
                if busca_nome == produtos['nome'].lower():  # Comparação insensível a maiúsculas/minúsculas
                    print(f'Este é o ID: {chave}')
                    print(f'Este é o nome: {produtos["nome"]}')
                    print(f'Este é o preço: {produtos["preco"]}')
                    print(f'Esta é quantidade: {produtos["qtd"]}')
                    print('É importado: ', end='')
                    if valor['importado']:
                        print('sim')
                    else:
                        print('não')
                    print('-'*40)
                    encontrado = True
                    break
            
                if not encontrado:
                    print('Este item não foi encontrado!') 

        elif busca == 'id':
            busca_id = int(input('Digite o ID do produto, por favor: ')).strip()

            # Verificando se o ID existe no dicionário
            if busca_id in produtos:
                print("-"*40)
                print(f'Produto com o ID:{produtos["busca_id"]} enontrado') 
                print(f'Este é o nome: {produtos["busca_id"]["nome"]}')
                print(f'Este é o preço: {produtos["busca_id"]["preco"]}')
                print(f'Esta é quantidade: {produtos["busca_id"]["qtd"]}')
                print('É importado: ', end='')
                if produtos['busca_id']['importado']:
                    print('sim')
                else:
                    print('não')
                print('-'*40)
            else:
                print("-"*40)
                print('Este item não foi encontrado!')
                print("-"*40)

        else:
            print("-"*40)
            print("Opção inválida! Digite 'nome' ou 'id'.")
            print("-"*40)

    elif proc_prod == 2:
        # Entrada do nome a ser procurado
        nome_proc = input('Digite por favor o nome do produto que você deseja verificar: ').strip().lower()

        # Lista de valores do dicionário
        lista_valores = list(produtos.values())

        # Função de troca
        def troca(L, i, j):
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

        # Função para ordenar (Selection sort)
        def selection_sort(lista):
            n = len(lista)  # Tamanho da lista
            for i in range(n):
                # Assume que o menor elemento está na posição i
                menor_indice = i
                # Procura pelo menor elemento no restante da lista
                for j in range(i + 1, n):
                    if lista[j]['nome'] < lista[menor_indice]['nome']:  # Ordenação por 'nome'
                        menor_indice = j
                # Troca usando a função troca
                troca(lista, i, menor_indice)

        # Ordenar a lista antes da busca binária
        selection_sort(lista_valores)

        # Função de busca binária
        def busca_binaria(lista, alvo):
            inicio = 0
            fim = len(lista) - 1

            while inicio <= fim:
                meio = (inicio + fim) // 2
                # Comparar o campo 'nome' do dicionário
                nome_atual = lista[meio]['nome'].lower()  # Padronizar para letras minúsculas
                if nome_atual == alvo:
                    return meio  # Retorna o índice do nome
                elif nome_atual < alvo:
                    inicio = meio + 1  # Procure na metade superior
                else:
                    fim = meio - 1  # Procure na metade inferior
            
            return -1  # Retorna -1 se o nome não foi encontrado

        # Buscar o nome fornecido pelo usuário
        resultado = busca_binaria(lista_valores, nome_proc)

        # Exibir o resultado
        if resultado != -1:
            print("-"*40)
            print(f"O produto '{nome_proc}' está no inventário!")
            print("-"*40)
        else:
            print("-"*40)
            print(f"O produto '{nome_proc}' não está no inventário...")
            print("-"*40)

    else :
        print("-"*40)
        print('Por favor digite apenas 1 ou 2!!')
        print("-"*40)

 

#Função vazia por enquanto - soso
def estatistica_inventario(produtos):
    pass

# Criando inventario Produtos
produtos = {}

#chamando a função crialogin() para começar o programa
crialogin()
