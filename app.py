#python usamos print('') 

#print('hello python')

# import da biblioteca
import os

def exibir_nome_do_programa():  
    print('Sabor Express\n')

def exibir_opcoes():
    print('1 - Cadastrar restautante')
    print('2 - Listar restaurante')
    print('3 - Ativar restautante')
    print('4 - Sair\n')

## em python nao precisa definir o tipo de uma variavel antes de usa-la
##e o método snake_case para variáveis,funções e métodos

#opcao_escolhida = input('Escolha uma opção:')

##def é uma function
#função para quando escolher a opcao 4 limpar o app
def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')


#por padrão,o python define os dados de entrada do input como string
#convertando p int
def escolher_opcao():

    opcao_escolhida = int(input('Ecolha uma opção :'))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizar_app()

#funcao que executa todas funcoes criadas 
def main():
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