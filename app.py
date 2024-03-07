# import da biblioteca
import os

#python tbm tem a tuplas,semelhante a array 
##lista de restaurantes
restaurantes = []


def exibir_nome_do_programa():  
    print('Sabor Express\n')


def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar restaurantes')
    print('4 - Sair\n')

## em python nao precisa definir o tipo de uma variavel antes de usa-la
##é recomendavel usar o método snake_case para variáveis,funções e métodos


##def é uma function
#função para quando escolher a opcao 4 limpar o app
def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

#função para retornar erro quando opção for invalida
def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()
    
# função para cadastrar um novo restaurante, e adicionar esse novo registro na lista/array de restaurantes
def cadastrar_novo_restaurante():
    os.system('cls')
    print(' *** Cadastro de novos restaurantes *** ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    input('Digite uma tecla para voltar ao menu principal.')
    main()



#por padrão,o python define os dados de entrada do input como string
#convertando p int
def escolher_opcao():

    try: 
        opcao_escolhida = int(input('Ecolha uma opção :'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()

    except: opcao_invalida()
 


def escolha_um_numero():

    numero_escolhido = int(input('Escolha um número , mostrarei se é impar ou par\n')) 

    if numero_escolhido % 2  == 0:
       print(f'O {numero_escolhido} é par')
    else:
        print(f'O {numero_escolhido} é impar')    
        
def validacao_login():    

    usuario_correto = "alura"
    senha_correta = "alura123"

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem sucedido!")
    else:
        print("Credenciais inválidas. Tente novamente.")
    




#funcao que executa todas funcoes criadas 
#def main é onde starta o programa,sendo esse o arquivo principal
#todas funcoes q precisam ser executadas precisam ficar dentro da funcao main
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__' :
    main()






























##meu_nome = 'Carol'
##minha_idade = '20 anos'

#print(f'Meu nome é {meu_nome} e eu tenho {minha_idade}.')

# Abordagem mais simples
#print('Meu nome é',meu_nome,'e tenho',minha_idade,'anos.')

# Abordagem do f-string
#print(f'Meu nome é {meu_nome} e tenho {minha_idade} anos.')

# Abordagem do .format()
#print('Meu nome é {} e tenho {} anos.'.format(meu_nome,minha_idade))



##print('A\nL\nU\nR\nA\n')

#valor_pi = 3.14159

#pi = 3.14159

## Maneiras de deixar arredondado numeros decimais,só duas casas
# Abordagem de f-string
##print(f'O valor arredondado de pi é: {valor_pi:.2f}')

# Abordagem de .format()
#print('O valor arredondado de pi é: {:.2f}'.format(valor_pi))

# Utilizando a função round()
#print('O valor arredondado de pi é:', round(valor_pi, 2))    