import hashlib
def crialogin(): #Função que começa o login do usuário. Cria ou apenas lê um arquivo 'login.txt'
    try: #Tenta abrir o arquivo 'login.txt para leitura, caso ele já tenha sido criado
        with open('login.txt', 'r') as a:
            autentica() #Chama a função 'autentica'
                     #A entrada do usuário é obrigatória 
    except FileNotFoundError:
        with open('login.txt', 'w+') as a: #Caso não exista o arquivo 'login.txt' ele cria um e permite a escrita
            usuario = input('Cadastre o nome do usuário:')
            usuario = hashlib.sha256(usuario.encode()).hexdigest() #Aplicando a função hash236 para o nome do usuário 
            senha = input('Cadastre a senha:')
            senha = hashlib.sha256(senha.encode()).hexdigest() #Aplicando a função hash236 para a senha do usuário 
            a.write(f'{usuario}\n{senha}\n') #Escrevendo a senha e o nome do usuário criptografado no arquivo login.txt
        menu() #Chama a função 'menu' visto que o após o primeiro acesso do usuário, não é preciso autenticar

def autentica(): #Função que autentica o login do usuário caso o arquivo login.txt já exista
    #Se o arquivo 'login.txt' está preenchido, essa função pede ao usuario as suas informações para autenticação
    #Função hash sempre resulta no mesmo valor para um conteúdo específico, assim conseguimos validar as entradas com o conteúdo do arquivo login.txt

    usuarioinput = input('Digite o nome do usuário:').strip() #Entrada do nome do usuário, ignorando espaços desnecessários
    usuarioinput = hashlib.sha256(usuarioinput.encode()).hexdigest() #Aplicando a mesma função hash236 para autenticação do nome do usuario 
    senhainput = input('Digite a senha:').strip() #Entrada da senha do usuário, ignorando espaços desnecessários
    senhainput = hashlib.sha256(senhainput.encode()).hexdigest() #Aplicando a mesma função hash236 para autenticação da senha do usuario 
    
    a = open('login.txt', 'r') #Abre o arquivo 'login.txt' apenas para leitura dos dados
    usuario = a.readline().strip() #Lê a primeira linha do arquivo login.txt e atribui a variável 'usuário'
    senha = a.readline().strip() #Lê a segunda linha do arquivo login.txt e atribui a variável 'senha'

    autenticacao = usuarioinput == usuario and senhainput == senha #variável 'autenticacao' vai receber a comparação das entradas 'usuarioinput' e 'senhainput'
                                                                           #Com o 'usuário  e 'senha' que já  estavam no arquivo 'login.txt', através da hash256
                                                                           #Ela retorna true ou false internamente
    if autenticacao: #Se a variável autenticacao for verdadeira, ou seja, login autenticado
        print(80 * '-')
        print('Autenticação bem-sucedida')
        print(80 * '-')
        menu() #Como o login foi autenticado, encaminhamos  o usuário para a função 'menu'
    else:
        print(80 * '-')
        print('Usuario ou senha incorretos. Tente novamente') #caso a autenticação não seja bem sucedida
        print(80 * '-')
        autentica() #Chama a função 'autentica' para o usuário tentar novamente
      
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
        
        #Solicita ao usuário uma decisão
        decisao = int(input('Escolha uma opção do menu de operações: '))
    
        if decisao == 1:
            redefinir_senha() #Caso a decisão seja igual a 1, o menu encaminha o usuário para redefinir senha
        elif decisao == 2:
            adiciona_item(produtos) #Caso a decisão seja igual a 2, o menu encaminha o usuário para adicionar um item ao inventário
        elif decisao == 3:
            remove_item(produtos) #Caso a decisão seja igual a 3, o menu encaminha o usuário para remover um item do inventário
        elif decisao == 4:
            atualiza_item(produtos) #Caso a decisão seja igual a 4, o menu encaminha o usuário para atualizar um item do inventário
        elif decisao == 5:
            exibe_inventario(produtos) #Caso a decisão seja igual a 5, o menu encaminha o usuário para vizualizar todo conteúdo do inventário
        elif decisao == 6:
            encontra_item(produtos) #Caso a decisão seja igual a 6, o menu encaminha o usuário para encontrar um produto do inventário
        elif decisao == 7:
            estatistica_inventario(produtos) #Caso a decisão seja igual a 7, o menu encaminha o usuário para vizualizar as estatísticas do inventário
        elif decisao == 8:
            print(80 * '-')
            print('Encerrando o programa... todos os dados do inventário serão perdidos.')
            print(80 * '-')
            break
        else:
            print('Essa opção não existe. Tente novamente') #Caso a decisão não seja nenhuma das opções acima o usuário não sai do menu e tem a opção de tentar novamente
        
def redefinir_senha():
    """Função que leva o usuário para outra autenticação de 'usuário' e 'senha', para assim coseguir redefinir a senha"""
    print(80 * '-')
    print("Para redefinir sua senha, autentique-se primeiro.")
    print(80 * '-')
    autentica2()  #Encaminhando para a autenticação 

def autentica2(): 
    """Função que autentica o login do usuário com o conteúdo do arquivo login.txt e o encaminha para alterar a senha"""
    #Função igual 'autentica()' mas apenas para a autentficação de redefir senha. Porque a outra função de autenticação leva o usuário para a função menu(), 
    # essa vai levar o usuário para a função senha_nova()
    usuario2 = input('Digite o nome de usuário atual: ').strip()
    usuario2 = hashlib.sha256(usuario2.encode()).hexdigest() #Aplicando a mesma função hash236 para autenticação do nome do usuário
    senha2 = input('Digite a senha atual: ').strip()
    senha2 = hashlib.sha256(senha2.encode()).hexdigest() #Aplicando a mesma função hash236 para autenticação da senha do usuário 
    
    
    a = open('login.txt', 'r')
    usuario = a.readline().strip() #lê a primeira linha criptografada do arquivo login.txt e atribui a variável 'usuário'
    senha = a.readline().strip() #lê a segunda linha criptografada do arquivo login.txt e atribui a variável 'senha'

    autenticacao = usuario2 == usuario and senha2 == senha #compara as entradas 'usuario2' e 'senha2' com 'usuario' e 'senha' que estão no arquivo login.txt - retorna True ou False
    if autenticacao: #Se a variável autenticacao for verdadeira
        print(40 * '-')
        print('Autenticação bem-sucedida')
        print(40 * '-')
        senha_nova() #após autenticação bem-sucedida o usuário pode definir uma senha nova
    else: #Se a variável autenticacao for falsa
        print(40 * '-')
        print('Usuario ou senha incorretos. Tente novamente')
        print(40 * '-')
        autentica2() # chama a função autentica2 para o usuário tentar novamente colocar as informações corretas

def senha_nova():
    """Função que permite o usuário redefinir a sua senha e atualiza as novas informações de usuário e senha no arquivo login.txt"""
    nova_senha = input('Digite a nova senha: ').strip() #usuário escreve a nova senha que ele deseja
    nova_senha_confirmacao = input('Confirme a nova senha: ').strip() # confirma a nova senha que ele quer

    if nova_senha == nova_senha_confirmacao: #Valida se o usuáro escreveu a nova senha corretamente
            usuario = input('Insira o nome do usuário atual: ') #pede o nome do usuário só para conseguir escrever no 'login.txt' de novo
            usuario = hashlib.sha256(usuario.encode()).hexdigest() #criptografa o usuário de novo para conseguir validar a entrada depois da redefinção da senha 
            nova_senha = hashlib.sha256(nova_senha.encode()).hexdigest() # criptografa a nova senha com hash 256
            a = open('login.txt', 'w') #abre o arquivo login.txt
            a.write(f'{usuario}\n{nova_senha}\n') #apaga tudo que tem no arquivo 'logn.txt' e escreve o usuário e a nova senha por cima
            print(40 * '-')
            print("Senha redefinida com sucesso!")
            print(40 * '-')
        
    else: #caso o usuáro tenha escrito a nova senha e a confirmação de formas diferentes, ele precisa fazer de novo
            print(60 * '-')
            print("As senhas novas não correspondem. Tente novamente.")
            print(60 * '-')
            senha_nova() #chama a própria função para o usuário tentar redefinir a senha da forma correta

def cesar(texto, chave=2, decriptar=False):
    """Função que aplica criptografia/decriptografia baseada em cifra de césar com deslocamento de 2 letras para cada letra de 'texto'. """
    if decriptar: #se decriptar for True o deslocamento é feito ao contrário para decriptar, caso não seja segue com a chave para criptografar
        chave = -chave
    L = list(texto) #o texto é transformado em lista e atribuido a uma variável para conseguir modificar cada indice(letra) da lista(texto)
    for i in range(len(L)): #para cada letra
        L[i] = chr(ord(L[i]) + chave) #transforma a letra no número correnpondente da tabela Unicode, soma com a chave = 2 e depois tranforma esse novo número para string novamente, que será a nova letra
    return ''.join(L) #depois de tranformar todas as letras separadamente, junta elas para formar a palavra criptografada

def adiciona_item(produtos):
    """Função que adiciona um novo item (chave:valor) com as informações de 'id', 'nome', 'quantidade', 'preço' e se é 'importado' ao inventário produtos"""

    while True:
            chave = input('Insira o ID do produto: ')
            if chave in produtos:
                    print("Erro: Este ID já existe no inventário. Tente novamente.")
            elif not chave:  # checa se o ID está vazio
                    print("Erro: O ID não pode estar vazio. Tente novamente.")
            elif not chave.isdigit(): #checa se o id é um número inteiro positivo
                    print('Erro: a entrada precisa ser um número inteiro positivo')
            else: 
                break #chave válida

    while True:
            nome = input('Insira o nome do produto: ').strip()#ignora espaços desnecessários
            if not nome: # checa se o nome está vazio
                print("Erro: O nome não pode estar vazio. Tente novamente.")
            else:
                break #nome válido

    while True:
            qtd = int(input('Insira a quantidade de unidades do produto: '))
            if qtd < 0:  # checa se qtd é um número inteiro positivo
                        print("Erro: A quantidade não pode ser negativa. Tente novamente.")
            else:
                break  # Quantidade válida
            
    while True:
            preco = float(input('Insira o preço do produto : '))
            if preco < 0:  # checa se qtd é um número positivo
                print("Erro: O preço não pode ser negativo. Tente novamente.")
            else:
                break # Preço válido
         
    while True:
            importado_input = input('O produto é importado? (s/n): ').strip().lower() #ignora espaços desnecessários e transforma letras em minúscula
            if importado_input not in ['s', 'n']: #checa se a entrada é 's' ou 'n'
                print("Erro: Digite 's' para sim ou 'n' para não.")
            else:
                importado = importado_input == 's'  # Converte para booleano a comparação da entrada com 's'(se for 's' = True, se não = False )
                break  # Entrada válida

    valor = { #criando um dicionário com conjunto de informações do produto, correspondente ao valor do par [chave][valor] do dicionário maior (ou seja, o inventário)
        'nome': nome, 
        'qtd': cesar(str(qtd)), #aplicando cifra de cesar para criptografar a quantidade de um produto
        'preco': cesar(str(preco)), #aplicando cifra de cesar para criptografar o preço de um produto
        'importado': importado
        }

    produtos[chave] = valor #atribuindo o valor a chave 

    print(80 * '-')
    print(f'{valor["nome"]} adicionado com sucesso ao inventário de produtos') #mostrando para o usuário o nome do produto que ele adicionou ao inventário
    print(80 * '-')

    menu()#Devolvendo o usuário ao menu de operação

def remove_item(produtos):
    """Função que remove um item do dicionário de produtos com o id como referência"""
    
    chave = input('Insira o ID do produto que deseja remover: ')
    
    if chave in produtos: #verifica se o id(chave) que o usuário inseriu ja existe no inventário produtos
        del produtos[chave] #função del remove um item do dicionário
        print(50 * '-') 
        print(f'Produto com ID {chave} removido com sucesso do inventário.')#mostrando para o usuário que o item, cujo id ele forneceu, foi removido
        print(50 * '-')
    else:
        print(50 * '-') 
        print(f'O produto com ID {chave} não existe no inventário.')#mostrando para o usuário que o item não existe no iventário
        print(50 * '-')

    menu()# Devolvendo o usuário ao menu de operação

def atualiza_item(produtos):
    """ Função que atualiza a informação (nome, quantidade, preço ou importado) de um item do inventário"""
    if not produtos: #Verifica se o inventário produtos é = False, ou seja, se está vazio
        print("O inventário está vazio. Nenhum produto para atualizar.")
        menu() #Já que está vazio, retorna o usuário para o menu de operações para tomar outra ação
        return

    chave = input('Digite o ID do produto que deseja atualizar: ').strip() #Solicita o ID do produto a ser atualizado e ignora espaços desnecessários

    if chave not in produtos: #Se a chave fornecida pelo usuário não estiver no inventário produtos
        print(50 * '-')
        print(f'O produto com ID {chave} não foi encontrado no inventário. Tente novamente atualizar outro produto')
        print(50 * '-')
        atualiza_item(produtos) #Já que o usuário forneceu um id que não existe, retorna o usuário para a mesma função para ele tentar encontrar novamente
        return

    produto = produtos[chave]  #Quando o id existe em produtos, atribui esse id as informações do produto correspondente
    print(50 * '-')
    print('Essas são as informações atuais do produto: ') #Exibe as informações atuais do produto:
    print(50 * '-')
    print(f"ID: {chave}") #Mostra o id que o usuário forneceu
    print(f"Nome: {produto['nome']}") #Mostra o nome do produto correspondente
    print(f"Quantidade: {cesar(produto['qtd'], decriptar=True)}") #Decifra a criptografia que foi gerada na quantidade desse produto quando ele foi adicionado, antes de exibir para o usuário
    print(f"Preço: {cesar(produto['preco'], decriptar=True)}")#Decifra a criptografia que foi gerada no preço desse produto quando ele foi adicionado, antes de exibir para o usuário
    print(f"Importado: {'Sim' if produto['importado'] else 'Não'}") #Mostra a informação sobre se é importado ou não do produto correspondente
    print(50 * '-')

    print("Quais informações você deseja atualizar?") 
    print("1. Nome")
    print("2. Quantidade")
    print("3. Preço")
    print("4. Importado")
    print("5. Voltar ao menu")
    opcao = int(input("Digite o número da opção desejada: ")) #Solicitar ao usuário os campos que ele deseja atualizar

    if opcao == 1:
        produto['nome'] = input('Digite o novo nome do produto: ').strip() #Se o usuário escolher 1, ele altera o nome do produto
    elif opcao == 2:
        produto['qtd'] = cesar(str(int(input('Digite a nova quantidade do produto: '))).strip()) #Se o usuário escolher 2, ele altera a qtd do produto, transforma em string e criptografa pra armazenar no inventário
    elif opcao == 3:
        produto['preco'] = cesar(str(float(input('Digite o novo preço do produto: '))).strip()) #Se o usuário escolher 3, ele altera o preço do produto, transforma em string e criptografa pra armazenar no inventário
    elif opcao == 4:
        importado = input('O produto é importado? (s/n): ').strip().lower() #Se o usuário escolher 4, ele muda se é importado(True) ou não(False)
        produto['importado'] = True if importado == 's' else False
    elif opcao == 5: 
        menu() #Se o usuário escolher 5, ele retorna ao menu de operações
        return
    else:
        print("Opção inválida. Tente novamente.") #Se o usuário não escolhe nenhuma das opções apresentadas ele volta para função e tenta novamente
        atualiza_item(produtos)
        return

    print(50 * '-') #Confirmar a atualização das informações do produto
    print("Produto atualizado com sucesso!")
    print(f"ID: {chave}") #Exibe o id que o usuário forneceu
    print(f"Nome: {produto['nome']}") #Exibe o nome do produto que o usuário atualizou ou o que já estava
    print(f"Quantidade: {cesar(produto['qtd'], decriptar=True)}") #Exibe decifrado a qtd do produto que o usuário atualizou ou o que já estava
    print(f"Preço: {cesar(produto['preco'], decriptar=True)}") #Exibe decifrado o preço do produto que o usuário atualizou ou o que já estava
    print(f"Importado: {'Sim' if produto['importado'] else 'Não'}") #Exibe a atualização de importado ou o valor que já estava
    print(50 * '-')
    
    menu() #Depois da atualização, retorna o usuário ao menu de operações

def bubble_sort(itens, chave): 
    """Ordena uma lista de dicionários ou tuplas alfabeticamente com Bubble Sort, usando a chave(item que é usado de referência para a ordenação)"""
    n = len(itens) #atribui o tamanho da lista de produtos para n
    for i in range(n): #controla o número de vezes que a lista é percorrida - que corresponde ao tamanho de n
        for j in range(0, n - i - 1): #percorre os pares adjacentes na lista e realiza a troca, se necessário.
            #Compara pelo valor da chave convertida para minúsculas (alfabética)
            if itens[j][1][chave].lower() > itens[j + 1][1][chave].lower():
                itens[j], itens[j + 1] = itens[j + 1], itens[j] #Se o elemento atual é maior que o próximo, eles trocam de posição.
    return itens #A função retorna a lista itens ordenada alfabeticamente por nome

def exibe_inventario(produtos):
    """Exibe os produtos do inventário ordenados alfabeticamente pelo nome."""
    if not produtos: #Se o inventário estiver vazio, produtos = False
        print('-' * 100)
        print("O inventário está vazio, não há produtos para exibir.")
        print('-' * 100)
        menu() #Usuário retorna ao menu de operações
        return
    
    #Caso o inventário produtos tenha conteúdo
    itens = list(produtos.items()) #Converte o dicionário para uma lista de tuplas (ID, informações do produto)

    itens_ordenados = bubble_sort(itens, 'nome') #Ordena os produtos pelo nome usando a função Bubble Sort

    #Exibe os produtos ordenados
    print(80 * '-')
    print("Lista de produtos do inventário em ordem alfabética:")
    print(80 * '-')
    for chave, valor in itens_ordenados:
        print(f"ID: {chave}") #Exibe o id do produto
        print(f"Nome: {valor['nome']}") #Exibe o nome do produto
        print(f"Quantidade: {cesar(valor['qtd'], decriptar=True)}")  #Exibe a quantiidade do produto decifrada
        print(f"Preço: R${float(cesar(valor['preco'], decriptar=True)):.2f}")  #Exibe o preço do produto decifrado
        print(f"Importado: ",'Sim' if valor['importado'] else 'Não') #Exibe a informação de importado
        print("-" * 40)

def encontra_item(produtos):
    """Função que encontra um item do inventário por nome ou id e retorna as informações do produto, ou apenas encontra o item pelo nome e retorna a existênca dele no iventário"""
    proc_prod = int(input('Digite 1 para uma busca detalhada ou 2 para verificar apenas a existência do produto: ')) #Dá a opção para o usuário encontrar um produto e saber suas informações ou apenas saber se ele existe no iventário

    if proc_prod == 1: #Caso o usuário escolha 1, ele terá uma busca detalhada
        busca = input("Você quer buscar um item pelo seu nome ou pelo ID? (Digite 'nome' ou 'id'): ").strip().lower() #o usuário pode encontrar o produto pelo nome ou pelo id
                                                                                                                     
        if busca == 'nome': #se o usuário preferiu a busca por nome
            busca_nome = input('Digite o nome do item: ').strip().lower() 
            encontrado = False #variável encontrado começa com o valor False

            for chave, valor in produtos.items(): #loop for que percorre cada produto(par chave:valor) do inventário
                if busca_nome == valor["nome"].lower(): #se o nome que o usuário colocou for o mesmo nome que exste em algum produto no inventário /transforma a entrada em letra minuscula
                    print('-' * 40)
                    print(f'{valor["nome"]} encontrado:') #retorna que encontrou o produto pelo nome
                    print('-' * 40) # e mostra as outrsa informações do produto encontrado:
                    print(f'Este é o ID: {chave}') #exibe o id
                    print(f'Esta é a quantidade: {cesar(valor['qtd'], decriptar=True)}') #exibe a quantdade decifrada
                    print(f'Este é o preço: R${float(cesar(valor['preco'], decriptar=True)):.2f}') #exibe o preço decifrado
                    print('É importado: ', 'sim' if valor['importado'] else 'não') #exibe se é importado ou não
                    print('-' * 40)
                    encontrado = True #já que o produto foi encontrado, a variável 'encontrado' recebe o valor True
                    menu() #chama o menu novamente depois que o usuário encontra o produto

            if not encontrado: #Caso encontrado continue como False depois do término do for
                print("-" * 80)
                print('Este item não foi encontrado. Tente novamente')
                print("-" * 80)
                encontra_item(produtos) #chama a função para ele tentar novamente

        elif busca == 'id':
            busca_id = input('Digite o ID do produto: ').strip()
            if busca_id in produtos: #se o id que o usuário colocar estiver no inventário
                valor = produtos[busca_id] #já que o id (chave) existe, ele acessa as informações do produto(valor)
                print('-' * 40)
                print(f'Produto com o ID {busca_id} encontrado:')
                print('-' * 40)
                print(f'Nome: {valor["nome"]}') #exibe nome do produto
                print(f'Quantidade: {cesar(valor['qtd'], decriptar=True)}') #exibe quantidade do produto decifrada
                print(f'Preço: R${float(cesar(valor['preco'], decriptar=True)):.2f}') #exibe preço do produto decifrado
                print('Importado: ', 'sim' if valor['importado'] else 'não') #exibe 'sim' se importado = True e 'não' se importado = 'False'
                print('-' * 40)
                menu() #chama o menu novamente depois que o usuário encontra o produto
            else: #se o usuário não digitou um id que está no inventário
                print("-" * 80)
                print('Este item não foi encontrado. Tente novamente')
                print("-" * 80)
                encontra_item(produtos) #chama a função para ele tentar novamente

        else: #se o usuário não digitou 'id' nem 'nome'
            print("-" * 50)
            print("Opção inválida! Tente novamente")
            print("-" * 50)
            encontra_item(produtos) #chama a mesma função para o usuário tentar novamente


    elif proc_prod == 2: #Caso o usuário escolha 2, ele terá apenas a informação de que o produto existe no iventário ou não
        nome_proc = input('Digite o nome do produto que você deseja verificar: ').strip().lower() #retira espaços desnecessários e deixa a letra minúscula
        lista_valores = list(produtos.values()) #transforma o inventário em uma lista de produtos

        def troca(L, i, j):
            """Função que troca a posição do indice 'i' e 'j' de uma lista 'L' """
            L[i], L[j] = L[j], L[i]

        def selection_sort(lista):
            """ Função que recebe uma lista e a ordena por ordem alfabética do nome dos produtos"""
            n = len(lista) # n recebe o tamanho da lista de produtos
            for i in range(n): #para cada produto(índice)
                menor_indice = i #define o primeiro índice como o menor
                for j in range(i + 1, n): #compara o primeiro índice com o segundo até chegar no final do tamanho lista
                    if lista[j]['nome'] < lista[menor_indice]['nome']: #se o nome do segundo índice(j) for menor(alfabeticamente) que o nome no primeiro índice, definido como 'menor_indice'
                        menor_indice = j # o menor indice vira o j
                troca(lista, i, menor_indice) #chama a função troca para trocar o j e o i de posição

        selection_sort(lista_valores) #implementação da função selection sort para organizar o inventário que foi transforadp em uma lista (lista_valores) e facilitar na busca

        encontrado = any(produto['nome'].lower() == nome_proc for produto in lista_valores) #função any retorna True ou False dependendo da comparação da entrada do usuário com os produtos do iventário 
        if encontrado: #se encontrado for True
            print('-' * 40)
            print("Produto encontrado no inventário!")
            print('-' * 40)
            menu() #retorna o usuário para o menu
        else: #se encontrado for False
            print('-' * 40)
            print("Produto não encontrado. Tente novamente")
            print('-' * 40)
            encontra_item(produtos) #retorna o usuério para a mesma função para tentar encontrar o produto novamente
    else:
        print('-' * 40)
        print('Por favor digite apenas um ou dois!')
        print('-' * 40)
        encontra_item(produtos)
        
def estatistica_inventario(produtos):
    """Função que exibe as estatísticas do inventário de produtos, como o valor, quantidade de produtos e quais são os produtos mais caros e mais baratos"""
    if not produtos: #Se o inventário tiver vazio
        print('-' * 80)
        print("O inventário está vazio. Não existe estatistica")
        print('-' * 80)
        menu() #Encaminha o usuário para o menu
        return
    
    #Caso o inventário não esteja vazio
    qtd_total = 0 #Define inicialmente a variável quantidade total zerada
    valor_total = 0  #Define inicialmente a variável valor total zerada
    mais_caro = None  #Define inicialmente a variável mais caro como None (valor nulo)
    mais_barato = None #Define inicialmente a variável mais caro como None (valor nulo)

    for id_produto, item in produtos.items():
        qtd = int(cesar(item['qtd'], decriptar=True))  #Atribui a qtd, a quantidade do produto decifrada
        preco = float(cesar(item['preco'], decriptar=True)) #Atribui a preço, o preço do produto decifrado 

        qtd_total += qtd #Soma qtd total com a qtd de cada produto do inventário que passa pelo for
        valor_total += qtd * preco #soma qtd total com a qtd de cada produto do inventário vezes o preço da unidade

        if mais_caro is None or preco > float(cesar(mais_caro['preco'], decriptar=True)): #Compara o preço de cada produto com o que está guardado em 'mais_caro'(que começa nulo)
            mais_caro = item #Se a comparação for maior, troca de posição

        if mais_barato is None or preco < float(cesar(mais_barato['preco'], decriptar=True)):
            mais_barato = item #Se a comparação for menor, troca de posição

    print("\n" + "*" * 50) #Exibindo as estatísticas do inventário
    print("╭───────────≪ INVENTÁRIO ≫───────────╮".center(50))
    print("*" * 50)
    print(f"Quantidade total de produtos: {qtd_total}") #Exibindo a quantidade total (contagem de produtos no inventário)
    print(f"Valor total do inventário: R${valor_total:.2f}") #Exibindo o valor monetário do inventário 
    print(f"Produto mais caro: {mais_caro['nome']} -> Preço: R${float(cesar(mais_caro['preco'], decriptar=True)):.2f}") #Exibindo o produto mais caro e o preço decifrado
    print(f"Produto mais barato: {mais_barato['nome']} -> Preço: R${float(cesar(mais_barato['preco'], decriptar=True)):.2f}")  #Exibindo o produto mais barato e o preço decifrado
    print("*" * 50)

    menu() #Retornando o usuário para o menu de operações

produtos = {} #criando dicionário produtos, que será nosso inventário, antes de começar o programa

crialogin() #chamando a função crialogin() para começar o programa
