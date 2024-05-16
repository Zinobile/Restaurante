import os

restaurantes = ["KFC", "BK", "MacDonalds", "Pizza Hut"]

def exibir_nome_do_programa():
   print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭━━┳╮╱╱╱╭╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱╱╱╱╰┫┣╯╰╮╱╱┃┃
┃╰━╯┣━━┫┃╭━━┳━┻╮╭╋━┳━━╮╱┃┣╮╭╋━━┫┃╭┳━━╮
┃╭━━┫╭╮┃┃┃┃━┫━━┫┃┃╭┫╭╮┃╱┃┃┃┃┃╭╮┃┃┣┫╭╮┃
┃┃╱╱┃╭╮┃╰┫┃━╋━━┃╰┫┃┃╭╮┃╭┫┣┫╰┫╭╮┃╰┫┃╭╮┃
╰╯╱╱╰╯╰┻━┻━━┻━━┻━┻╯╰╯╰╯╰━━┻━┻╯╰┻━┻┻╯╰╯""")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
   
def finalizar_app():
    print("\nFinalizando ...")
 
def opcao_invalida():
    print("\nDesculpe!Não temos essa opção em nosso sistema.\n")
    input("Digite enter para voltar ao menu principal")  
    main()

def cadastrar_novo_restaurante():
    print("Cadastrar restaurante")
    os.system("cls")
    print("cadastro de novos restaurante\n ")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ")


def listar_restaurante():
    #print(f"Listando restaurantes de oz/n",{restaurantes})

    for restaurante in restaurantes:
        print(f"--{restaurante}")
    input('Digite uma tecla para voltar ao menu pricipal')
    main()

def escolher_opção():
    try:
        opcao = int(input("\nEscolha uma opção: "))
       
        if(opcao == 1):
            cadastrar_novo_restaurante()

        elif(opcao == 2):
            listar_restaurante()
            #print("Listar restaurantes")
               
        elif(opcao == 3):
            print("Ativar restaurante")
               
        elif(opcao == 4):
            finalizar_app()
           
        else:
            opcao_invalida()
    except:
        opcao_invalida()

   
def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu()
    escolher_opção()
   
if __name__ == '__main__':
    main()