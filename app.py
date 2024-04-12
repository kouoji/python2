import os

def finalizar_app():
    os.system("cls")
    print("Finalizando o app\n")

def escolher_opcoes():
    print("Programa Expresso")
    print("*****************")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def chamar_nome_do_app():
    print("Restaurante Expressao\n")

def main():
    escolher_opcoes()
    chamar_nome_do_app()
    opcaodigitada = input("Digite a opção desejada: ")

    if opcaodigitada == '1':
        print("Você escolheu cadastrar restaurante")
    elif opcaodigitada == '2':
        print("Você escolheu listar restaurante")
    elif opcaodigitada == '3':
        print("Você escolheu ativar restaurante")
    elif opcaodigitada == '4':
        print("Você escolheu sair do aplicativo")
    else:
        print("Você escolheu sair do app")

if __name__ == "__main__":
    finalizar_app()
    main()