from modulos import pets
from modulos import validacao 
from modulos import memoria

def cadastrodeUsuarios():

    print("\n", "-" * 60)
    print("CADASTRO DE USUÁRIOS")

    print("\nPOR FAVOR, PREENCHA AS INFORMAÇÕES A SEGUIR:\n")

    print("\n EXEMPLO DE NOME: JOAO SILVA")
    nome = input("\nDIGITE SEU NOME COMPLETO (SEM ACENTUAÇÃO): ")

    while not validacao.verificaVazio(nome):

        nome = input("\nDIGITE SEU NOME COMPLETO: ")

    CPF = input("\nDIFITE SEU CPF (APENAS NÚMEROS): ")

    while not validacao.verificaVazio(CPF) or not validacao.verificaCPF(CPF) or not validacao.verificaCPFRepetido(CPF):

        CPF = input("\nDIGITE SEU CPF (APENAS NÚMEROS): ")

    email = input("\nDIGITE SEU EMAIL: ")

    while not validacao.verificaVazio(email) or not validacao.verificaEmail(email) or not validacao.verificaEmailRepetido(email):

        email = input("\nDIGITE SEU EMAIL: ")

    numero = input("\nDIGITE SEU NÚMERO DE TELEFONE (APENAS NÚMEROS): ")

    while not validacao.verificaVazio(numero) or not validacao.verificaNumero(numero):

        numero = input("\nDIGITE SEU NÚMERO DE TELEFONE (APENAS NÚMEROS): ")

    idade = input("\nDIGITE SUA IDADE: ")

    while not validacao.verificaVazio(idade) or not validacao.verificaIdade(idade):

        idade = input("\nDIGITE SUA IDADE: ")

    senha = input("\nDIGITE SUA SENHA DE ACESSO: ")

    while not validacao.verificaVazio(senha) or not validacao.verificaSenha(senha):

        senha = input("\nDIGITE SUA SENHA DE ACESSO: ")

    verificacao = input("\nDIGITE O SEU PERSONAGEM PREFERIDO NA INFÂNCIA PARA QUESTÕES DE VERIFICAÇÃO: ")

    while not validacao.verificaVazio(verificacao):

        verificacao = input("\nDIGITE O SEU PERSONAGEM PREFERIDO NA INFÂNCIA PARA QUESTÕES DE VERIFICAÇÃO: ")

    opcao = input("\nVOCÊ É COLABORADOR DO PETSHOP? (S/N): ")

    while not validacao.verificaVazio(opcao) or not validacao.verificaBoolean(opcao):

        opcao = input("\nVOCÊ É COLABORADOR DO PETSHOP? (S/N): ")

    if (opcao.upper() == 'S'):

        tentativas = 0

        while tentativas < 3:

            valida = validacao.verificaSenhaColaborador()

            if (valida == True):

                logado = True
                tipoUsuario = 'colaborador'

                memoria.salvarColaborador(nome, CPF, email, numero, idade, senha, verificacao, logado, tipoUsuario)

                print("\nCADASTRO DE COLABORADOR E LOGIN FEITOS COM SUCESSO!")

                break

            else:

                tentativas += 1

                print(f"\nSENHA DE VERIFICAÇÃO INVÁLIDA! TENTATIVAS RESTANTES: {3 - tentativas}")

                if tentativas == 3:

                    print("\nNÚMERO MÁXIMO DE TENTATIVAS ALCANÇADO! CADASTRO DE COLABORADOR NÃO REALIZADO.")

                    break

    else:

        idPet = []
        tipoUsuario = ''

        while True:

            opcao = input("\nVOCÊ DESEJA REALIZAR O CADASTRO DE ALGUM PET? (S/N): ")

            while not validacao.verificaVazio(opcao) or not validacao.verificaBoolean(opcao):

                opcao = input("\nVOCÊ DESEJA REALIZAR O CADASTRO DE ALGUM PET? (S/N): ")

            if (opcao.upper() == 'S'):

                id = pets.cadastroPet()

                idPet.append(id)

            else:

                tipoUsuario = 'cliente'

                break

        logado = True
        memoria.salvarCliente(nome, CPF, email, numero, idade, senha, verificacao, logado, tipoUsuario, idPet)

        print("\nCADASTRO DE CLIENTE REALIZADO E LOGIN FEITOS COM SUCESSO!")

    return None

def loginUsuario():

    print("\n", "-" * 60)
    print("LOGIN DE USUÁRIOS")

    email = input("\nDIGITE SEU EMAIL: ")

    while not validacao.verificaVazio(email):

        email = input("\nDIGITE SEU EMAIL: ")

    senha = input("\nDIGITE SUA SENHA DE ACESSO: ")

    while not validacao.verificaVazio(senha):

        senha = input("\nDIGITE SUA SENHA DE ACESSO: ")

    opcao = input("\nVOCÊ É COLABORADOR DO PETSHOP? (S/N): ")

    while not validacao.verificaVazio(opcao) or not validacao.verificaBoolean(opcao):

        opcao = input("\nVOCÊ É COLABORADOR DO PETSHOP? (S/N): ")

    if (opcao.upper() == 'S'):

        tentativas = 0

        while tentativas < 3:

            valida = validacao.verificaSenhaColaborador()

            if (valida == True):

                memoria.atualizarLoginLogout(True, email, senha)

                print("\nLOGIN REALIZADO COM SUCESSO!")

                break

            else:

                tentativas += 1

                print(f"\nSENHA DE VERIFICAÇÃO INVÁLIDA! TENTATIVAS RESTANTES: {3 - tentativas}")

                if tentativas == 3:

                    print("\nNÚMERO MÁXIMO DE TENTATIVAS ALCANÇADO! CADASTRO DE COLABORADOR NÃO REALIZADO.")

                    break

    else:

        memoria.atualizarLoginLogout(True, email, senha)

        print("\nLOGIN REALIZADO COM SUCESSO!")

    return None

def logoutUsuario(usuario):

    print("\n", '-' * 60)
    print("LOGOUT DE USUÁRIOS")

    opcao = input("\nVOCÊ DESEJA REALMENTE FAZER LOGOUT DA SUA CONTA? (S/N): ")

    while not validacao.verificaVazio(opcao) or not validacao.verificaBoolean(opcao):

        opcao = input("\nVOCÊ DESEJA REALMENTE FAZER LOGOUT DA SUA CONTA? (S/N): ")

    if (opcao.upper() == 'S'):

        memoria.atualizarLoginLogout(False, usuario['email'], usuario['senha'])

    else:

        print("\nLOGOUT CANCELADO PELO USUÁRIO!")

    return None

