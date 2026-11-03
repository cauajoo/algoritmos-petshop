from modulos import validacao

def menuInicial():

    print("\n", "-" * 60)
    print("BEM-VINDO AO PET.PY - AMOR E CUIDADO EM CADA LINHA!")

    print("\nEXPLORE OS MENUS ABAIXO:")
    print("\n1 - CADASTRO DE USUARIOS  " \
    "\n2 - LOGIN " \
    "\n3 - PET-SERVIÇOS E PRODUTOS " \
    "\n4 - SAIR DA CONTA " \
    "\n0 - ENCERRAR SISTEMA")

    menu_1 = input("\nDIGITE SUA ESCOLHA: ")

    while not validacao.verificaVazio(menu_1):

        menu_1 = input("\nDIGITE SUA ESCOLHA: ")

    return menu_1

def menuProdutoseServicos(logado, tipoUsuario):

    if logado == 'True' and tipoUsuario == 'colaborador':

        print("\n", "-" * 60)
        print("PET-SERVIÇOS E PRODUTOS")
        print("ÁREA DO ADMINISTRADOR")

        print("\nEXPLORE OS MENUS ABAIXO:")
        print("\n1 - CADASTRAR PRODUTO " \
        "\n2 - CADASTRAR SERVIÇOS " \
        "\n3 - ATUALIZAR PRODUTO OU SERVIÇOS " \
        "\n4 - BUSCAR " \
        "\n5 - REMOVER PRODUTO OU SERVIÇOS " \
        "\n6 - HISTÓRICO DE VENDAS E AGENDAMENTO " \
        "\n7 - LISTAR PRODUTOS E SERVIÇOS CADASTRADOS"
        "\n0 - VOLTAR PARA O MENU INICIAL")

        menu_2 = input("\nDIGITE SUA ESCOLHA: ")

        while not validacao.verificaVazio(menu_2):

            menu_2 = input("\nDIGITE SUA ESCOLHA: ")

        return menu_2

    elif logado == 'True' and tipoUsuario == 'cliente':

        print("\n", "-" * 60)
        print("PET-SERVIÇOS E PRODUTOS")
        print("ÁREA DO USUÁRIO")

        print("\nEXPLORE OS MENUS ABAIXO:")
        print("\n1 - COMPRAR PRODUTO " \
        "\n2 - AGENDAR SERVIÇOS " \
        "\n3 - BUSCAR " \
        "\n4 - PETS " \
        "\n0 - VOLTAR PARA O MENU INICIAL")

        menu_2 = input("\nDIGITE SUA ESCOLHA: ")

        while not validacao.verificaVazio(menu_2):

            menu_2 = input("\nDIGITE SUA ESCOLHA: ")

        return menu_2

def menuTipoProduto():

    tiposProduto = {

        '0': 'HIGIENE',
        '1': 'ALIMENTACAO',
        '2': 'RECREACAO',
        '3': 'MEDICAMENTOS',
        '4': 'OUTROS' 
    }

    while True:

        print("\n", "-" * 60)
        print("TIPO DO PRODUTO")

        print("\nMENU TIPO DO PRODUTO: \n" \
        "\n0 - HIGIENE " \
        "\n1 - ALIMENTAÇÃO " \
        "\n2 - RECREAÇÃO " \
        "\n3 - MEDICAMENTOS " \
        "\n4 - OUTROS \n")

        menu_3 = input("\nDIGITE A OPÇÃO ESCOLHIDA: ")

        while not validacao.verificaVazio(menu_3):

            menu_3 = input("\nDIGITE SUA ESCOLHA: ")

        if menu_3 in tiposProduto:

            return tiposProduto[menu_3]

        print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!")

def menuAtualizar():

    print("\n", "-" * 60)
    print("ATUALIZAR PRODUTOS E SERVIÇOS")

    print("\nMENU: \n" \
    "\n1 - ATUALIZAR PRODUTOS " \
    "\n2 - ATUALIZAR SERVIÇOS " \
    "\n0 - VOLTAR PARA O MENU DA ÁREA DO ADMINISTRADOR\n")

    menu_3 = input("\nDIGITE A OPÇÃO ESCOLHIDA: ")

    while not validacao.verificaVazio(menu_3):

        menu_3 = input("\nDIGITE SUA ESCOLHA: ")

    return menu_3

def menuRemover():

    print("\n", "-" * 60)
    print("REMOVER PRODUTOS E SERVIÇOS")

    print("\nMENU: \n" \
    "\n1 - REMOVER PRODUTOS " \
    "\n2 - REMOVER SERVIÇOS " \
    "\n0 - VOLTAR PARA O MENU DA ÁREA DO ADMINISTRADOR\n")

    menu_3 = input("\nDIGITE A OPÇÃO ESCOLHIDA:")

    while not validacao.verificaVazio(menu_3):

        menu_3 = input("\nDIGITE SUA ESCOLHA: ")

    return menu_3

def menuBuscar():

    print("\n", "-" * 60)
    print("BUSCAR PRODUTOS E SERVIÇOS")

    print("\nMENUS: \n" \
    "\n1 - PRODUTOS " \
    "\n2 - SERVIÇOS " \
    "\n3 - VOLTAR PARA A ÁREA DO USUÁRIO \n")

    menu_3 = input("\nDIGITE A OPÇÃO ESCOLHIDA: ")

    while not validacao.verificaVazio(menu_3):

        menu_3 = input("\nDIGITE SUA ESCOLHA: ")

    return menu_3

def menuPets():

    print("\n", "-" * 60)
    print("PETS")

    print("\nMENU: \n" \
    "\n1 - LISTAR PETS"
    "\n2 - ADICIONAR PETS" \
    "\n3 - REMOVER PETS" \
    "\n0 - VOLTAR PARA A ÁREA DE USUÁRIO \n")

    menu_3 = input("\nDIGITE A OPÇÃO ESCOLHIDA: ")

    while not validacao.verificaVazio(menu_3):

        menu_3 = input("\nDIGITE SUA ESCOLHA: ")

    return menu_3



