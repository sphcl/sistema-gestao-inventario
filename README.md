# Sistema de gestão de inventário
## Funcionalidades:
###   •1º Login e autenticação: A pessoa que estiver executando o programa precisa inserir um usuário e senha para acessar o inventário.
####     - O usuário e a senha devem ser armazenados no arquivo de texto utilizando criptografia hashing (SHA-256) 

###   •2º Menu de operações. Após a pessoa ser autenticada pelo login, ela terá acesso ao menu de operações no terminal.
####     - O menu de operações precisa ter as seguintes funções: 
#####        1. Redefinir Login e senha: função que permite sobrescrever o usuário e senha que foram cadastrados no primeiro acesso e salvos no arquivo login.txt, usando criptografia SHA-256 para a redefinição de senha  
#####        2. Adicionar produtos ao inventário: dicionário para armazenar as informações do inventário, função que permita adicionar um produto, no final da função deve mostrar na tela “produto adicionado com sucesso” e devolver o usuário para o menu de operações.
#####        3. Remover produtos do inventário: função que permita remover um produto do inventário, no final da função deve mostrar na tela “produto removido com sucesso” e devolver o usuário para o menu de operações. 
#####        4. Atualizar (editar) produtos do inventário: função que permita editar um produto existente (através do nome ou ID) no inventário, no final da função deve mostrar na tela “produto atualizado com sucesso” e devolver o usuário para o menu de operações.
#####        5. Exibir todos produtos cadastrados (ordenados por nome) no inventário: função que puxa todos os registros do dicionário (inventário), descriptografa com cifra de césar e exibe para o usuário ordenados por nome usando algoritmo de ordenação.
#####        6. Encontrar produto por ID ou nome:  função que encontra um produto existente pelo ID ou nome, no inventário e exiba para o usuário, final da função deve retornar “produto encontrado” e em seguida exibir o produto, ou “produto não encontrado”. Depois devolver o usuário para o menu de operações caso ele aperte 1. 
#####        7. Exibir as estatísticas do inventário: função que conte quantos produtos tem no inventário e que 		some o valor total do inventário.   
#####        8. Sair do menu de operações 


### Linguagens utilizada:
#### •Python 3.12.5

### Biblioteca utilizada:
#### Ainda em desenvolvimento.

![projetoEmDesenvolvimento](https://github.com/user-attachments/assets/5140dfd0-2914-4e01-9c08-4d6461a09dde)

