from modulos import menus
from modulos import usuarios
from modulos import validacao
from modulos import memoria
from modulos import produtos
from modulos import servicos
from modulos import pets

memoria.resetarUsuariosLogados()

while True:

    opcao = menus.menuInicial()
    usuario = validacao.verificaUsuarioLogado()

    if opcao == '1':

        if usuario is not None:

            print(f"\nUSUÁRIO {usuario['nome']} LOGADO! POR FAVOR, FAÇA O LOGOUT ANTES DE REALIZAR UM NOVO CADASTRO.")

        else:

            usuarios.cadastrodeUsuarios()

    elif opcao == '2':

        if usuario is not None:

            print(f"\nUSUÁRIO {usuario['nome']} LOGADO! POR FAVOR, FAÇA O LOGOUT ANTES DE REALIZAR UM NOVO LOGIN.")
        
        else:

            usuario = usuarios.loginUsuario()

    elif opcao == '3':

        if usuario is None:

            print("\nNENHUM USÚARIO ESTÁ LOGADO NO MOMENTO! POR FAVOR, FAÇA O LOGIN ANTES DE ACESSAR O MENU DO PET SHOP.")

        else:

            while True:

                if usuario['tipoUsuario'] == 'colaborador':

                    opcao_1 = menus.menuProdutoseServicos(usuario['logado'], usuario['tipoUsuario'])

                    if opcao_1 == '1':

                        produtos.cadastrarProdutos()

                    elif opcao_1 == '2':

                        servicos.cadastrarServicos()

                    elif opcao_1 == '3':

                        while True:

                            opcao_2 = menus.menuAtualizar()

                            if opcao_2 == '1':

                                produtos.atualizarProduto()

                            elif opcao_2 == '2':

                                servicos.removerServicos()

                            elif opcao_2 == '0':

                                print("\nVALTANDO PARA ÁREA DO USUARIO...")
                                break

                            else:

                                print("\nOPÇÃO INVÁLIDA!")

                    elif opcao_1 == '4':

                        memoria.busca()

                    elif opcao_1 == '5':

                        while True:

                            opcao_2 = menus.menuRemover()

                            if opcao_2 == '1':

                                produtos.removerProduto()

                            elif opcao_2 == '2':

                                servicos.removerServicos()

                            elif opcao_2 == '0':

                                print("\nVALTANDO PARA ÁREA DO USUARIO...")
                                break

                            else:

                                print("\nOPÇÃO INVÁLIDA!")

                    elif opcao_1 == '6':

                        memoria.listarCompEServ()

                    elif opcao_1 == '7':

                        produtos.listarProdutos()
                        servicos.listarServicos()

                    elif opcao_1 == '0':

                        print("\nVOLTANDO PARA O MENU INICIAL...")

                        break

                    else:

                        print("\nOPÇÃO INVÁLIDA!")

                elif usuario['tipoUsuario'] == 'cliente':

                    opcao_1 = menus.menuProdutoseServicos(usuario['logado'], usuario['tipoUsuario'])

                    if opcao_1 == '1':

                        produtos.comprarProduto(usuario)

                    elif opcao_1 == '2':

                        servicos.agendarServicos(usuario)

                    elif opcao_1 == '3':

                        memoria.busca()

                    elif opcao_1 == '4':

                        while True:

                            opcao_2 = menus.menuPets()

                            if opcao_2 == '1':

                                pets.listarPet(usuario)

                            elif opcao_2 == '2':

                                idPet = pets.cadastroPet()

                                memoria.atualizarCliente(idPet, usuario)

                            elif opcao_2 == '3':

                                memoria.removerPet()

                            elif opcao_2 == '0':

                                print("\nVOLTANDO PARA O MENU ANTERIOR...")

                                break

                            else:

                                print("\nOPÇÃO INVÁLIDA!")

                    elif opcao_1 == '0':

                        print("\nVOLTANDO PARA O MENU INICIAL...")

                        break

                    else:

                        print("\nOPÇÃO INVÁLIDA!")

    elif opcao == '4':

        if usuario is None:

            print("\nNENHUM USUÁRIO ESTÁ LOGADO NO MOMENTO! POR FAVOR, FAÇA O LOGIN ANTES DE REALIZAR O LOGOUT.")

        else:

            usuarios.logoutUsuario(usuario)

            usuario = None

    elif opcao == '0':

        print("\nENCERRANDO SISTEMA... ATÉ LOGO!")

        break

    else:

        print("\nOPÇÃO INVÁLIDA! POR FAVOR, TENTE NOVAMENTE.")


