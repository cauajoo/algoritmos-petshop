logado = False
usuario = [['Cauã', '00099933350', 'caua@', '83988887777', '20', '12345678*', 'Homem de Ferro', [['Cachorro', 'Mel', 'Labrador', '8', '20', 'S']]]]
chaveTipo = 0
indiceUsuario = 0
usuarioAdmin = [['Pedro', '11122233344', 'pedro@', '83911112222', '20', '11223344*', 'Hulk']]
indiceUsuarioAdmin = 0
chaveSegurancaAdmin = "35897122"
produtos = [['Ração 100g', 'ALIMENTAÇÃO', 25.5, 20], ['Shampoo para Cachorro', 'HIGIENE', 15.0, 10]]
servicos = [['Consulta', 350.0, [['12/12/2025', ['10:00', '12:00', '14:00']], ['15/12/2025', ['12:00', '14:00', '16:00']]]]]
encomendas = []
agendamentos = []

while (True):

    print("\n--------------------------------------------------------------------------------------------")
    print("BEM-VINDO AO PET.PY - AMOR E CUIDADO EM CADA LINHA!")
    print("\nEXPLORE OS MENUS ABAIXO:")
    print("\n1 - CADASTRO DE USUARIOS \n2 - LOGIN \n3 - PET-SERVIÇOS E PRODUTOS \n4 - SAIR DA CONTA \n0 - ENCERRAR SISTEMA")

    opcao_0 = input("\nDIGITE SUA ESCOLHA: ")

    if (opcao_0 == '1'):

        while (True):

            if logado == True:

                print("--------------------------------------------------------------------------------------------")
                print("CADASTRO DE USUARIOS")

                print("\nPARA REALIZAR OUTRO CADASTRO SAIA DA CONTA!")
                break

            else:

                print("--------------------------------------------------------------------------------------------")
                print("CADASTRO DE USUARIOS")

                nome = input("\nINFORME SEU NOME: ").strip()

                while (nome == ""):

                    print("NOME INVÁLIDO!")
                    nome = input("\nINFORME SEU NOME NOVAMENTE: ").strip()
                
                cpf = input("\nINFORME SEU CPF (SÓ NUMEROS): ").strip()

                while ((cpf == "") or (len(cpf) != 11)):

                    print("CPF INVÁLIDO!")
                    cpf = input("\nDIGITE NOVAMENTE SEU CPF: ").strip()

                email = input("\nINFORME SEU EMAIL: ").strip()

                while ((email == "") or ('@' not in email)):

                    print("EMAIL INVÁLIDO!")
                    email = input("\nINFORME SEU EMAIL NOVAMENTE: ").strip()

                telefone = input("\nINFORME SEU TELEFONE (SÓ NUMEROS): ").strip()

                while ((telefone == "") or (len(telefone) != 11)):

                    print("TELEFONE INVÁLIDO!")
                    telefone = input("\nINFORME SEU TELEFONE NOVAMENTE: ").strip()

                idade = input("\nINFORME SUA IDADE: ").strip()

                while (idade == ""):

                    print("IDADE INVÁLIDA!")
                    idade = input("\nINFORME SUA IDADE NOVAMENTE: ").strip()

                print("\nA SENHA DEVE CONTER NO MÍNIMO 8 DIGITOS E UM CARACTER ESPECIAL !@#*")

                senha = input("DIGITE UMA SENHA: ").strip()

                while ((len(senha) < 8) or (('*' not in senha) and ('#' not in senha) and ('@' not in senha) and ('!' not in senha))):

                    print("SENHA INVÁLIDA!")
                    senha = input("DIGITE NOVAMENTE UMA SENHA:").strip()

                verificacao = input("\nPARA FINS DE VERIFICAÇÃO, QUAL FOI SEU PERSONAGEM FAVORITO NA INFÂNCIA: ").strip()

                while (verificacao == ""):

                    print("INVÁLIDO!")
                    verificacao = input("\nINFORME NOVAMENTE: ").strip()

                print("--------------------------------------------------------------------------------------------")

                tpUsrio = input("\nVOCÊ É COLABORADOR PET.PY (S/N)? ").strip().upper()

                while ((tpUsrio not in ['S', 'N'])):

                    print("OPÇÃO INVÁLIDA!")
                    tpUsrio = input("\nDIGITE NOVAMENTE: ").strip().upper()
                
                if (tpUsrio == 'N'):

                    usuario.append([nome, cpf, email, telefone, idade, senha, verificacao])

                    logado = True
                    chaveTipo = 1
                    indiceUsuario = len(usuario) - 1

                    opcao_1 = input("\nDESEJA REALIZAR O CADASTRO DO SEU PET (S/N)? ").strip().upper()

                    while ((opcao_1 not in ['S', 'N'])):

                        print("OPÇÃO INVÁLIDA!")
                        opcao_1 = input("\nDIGITE NOVAMENTE: ").strip().upper()
                    
                    if (opcao_1 == 'S'):

                        petUsuario = []

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("CADASTRO DE PETS")

                            tipoPet = input("\nQUAL TIPO DE ANIMAL É O SEU PET? ").strip()

                            while (tipoPet == ""):

                                print("OPÇÃO VAZIA!")
                                tipoPet = input("\nDIGITE NOVAMENTE: ").strip()
                        
                            nomePet = input("\nINFORME O NOME DO SEU PET: ").strip()

                            while (nomePet == ""):

                                print("NOME INVÁLIDO")
                                nomePet = input("\nINFORME O NOME NOVAMENTE: ").strip()

                            racaPet = input("\nINFORME A RAÇA DO SEU PET (SE NÃO HOUVER DIGITE 'RND'): ").strip()

                            while (racaPet == ""):

                                print("RAÇA INVÁLIDA")
                                racaPet = input("\nINFORME A RAÇA NOVAMENTE: ").strip()

                            idadePet = input("\nINFORME A IDADE DO SEU PET: ").strip()

                            while (idadePet == ""):

                                print("IDADE INVÁLIDA!")
                                idadePet = input("\nINFORME A IDADE NOVAMENTE: ").strip()
                        
                            pesoPet = input("\nINFORME O PESO DO SEU PET: ").strip()

                            while (pesoPet == ""):

                                print("PESO INVÁLIDO!")
                                pesoPet = input("\nINFORME O PESO NOVAMENTE: ").strip()

                            vacina = input("\nAS VACINAS DO SEU PET ESTÃO EM DIA (S/N)? ").strip().upper()

                            while ((vacina not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                vacina = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            petUsuario.append([tipoPet, nomePet, racaPet, idadePet, pesoPet, vacina])

                            opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRO ANIMAL (S/N)? ").strip().upper()

                            while ((opcao_2 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_2 == 'N'):

                                print("\nCADASTRO(S) DO(S) PET(S) REALIZADO!")
                                break     
                    
                        usuario[-1].append(petUsuario)

                    print("\nCADASTRO(S) REALIZADO(S) E USUÁRIO LOGADO!")
                    break

                else:

                    tentativa = 3

                    while tentativa != 0:

                        opcao_3 = input("\nDIGITE A CHAVE DE VERIFICAÇÃO DE ADMINS: ").strip()

                        while (opcao_3 == ""):

                            print("OPÇÃO VAZIA!")
                            opcao_3 = input("\nDIGITE NOVAMENTE: ").strip()

                        if (opcao_3 == chaveSegurancaAdmin):

                            usuarioAdmin.append([nome, cpf, email, telefone, idade, senha, verificacao])

                            logado = True
                            chaveTipo = 2
                            indiceUsuarioAdmin = len(usuarioAdmin) - 1

                            print("\nCADASTRO REALIZADO, E USUÁRIO LOGADO!")
                            break
                        
                        else: 

                            tentativa -= 1
                            print(f"\nCHAVE INCORRETA! VOCÊ SÓ TEM {tentativa} TENTATIVAS, DIGITE NOVAMENTE!")

                            if ((tentativa == 0) and (logado == False)):

                                print("\nCADASTRO NÃO REALIZADO!")
                                break

                    break

    elif (opcao_0 == '2'):

        if logado == True:

            print("--------------------------------------------------------------------------------------------")
            print("LOGIN")

            print("\nUSUARIO LOGADO!\n")

        else:

            while True:

                print("\n--------------------------------------------------------------------------------------------")
                print("LOGIN")

                opcao_1 = input("\nVOCÊ É COLABORADOR PET.PY (S/N)? ").strip().upper()

                while ((opcao_1 not in ['S', 'N'])):

                    print("OPÇÃO INVÁLIDA!")
                    opcao_1 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                email = input("\nINFORME SEU EMAIL PARA LOGIN: ").strip()

                while (email == ""):

                    print("VALOR INVÁLIDO!")
                    email = input("\nDIGITE NOVAMENTE: ").strip()

                opcao_4 = input("\nDESEJA RECUPERAR SENHA (S/N)? ").strip().upper()

                while ((opcao_4 not in ['S', 'N'])):

                    print("OPÇÃO INVÁLIDA!")
                    opcao_4 = input("\nDIGITE NOVAMENTE: ").strip().upper()
                
                if (opcao_4 == 'S'): 

                    cpf = input("\nINFORME SEU CPF (SÓ NUMEROS): ").strip()

                    while ((cpf == "") or (len(cpf) != 11)):

                        print("CPF INVÁLIDO!")
                        cpf = input("\nDIGITE NOVAMENTE SEU CPF: ").strip()

                    verificacao = input("\nQUAL FOI SEU PERSONAGEM FAVORITO NA INFÂNCIA: ").strip()

                    while (verificacao == ""):

                        print("INVÁLIDO!")
                        verificacao = input("\nINFORME NOVAMENTE: ").strip()

                    achou = False

                    for i in range(len(usuario)):

                        if ((cpf == usuario[i][1]) and (verificacao == usuario[i][6])):

                            achou = True

                            print("\nA SENHA DEVE CONTER NO MÍNIMO 8 DIGITOS E UM CARACTER ESPECIAL !@#*")

                            senha = input("DIGITE UMA SENHA: ").strip()

                            while ((len(senha) < 8) or (('*' not in senha) and ('#' not in senha) and ('@' not in senha) and ('!' not in senha))):

                                print("SENHA INVÁLIDA!")
                                senha = input("DIGITE NOVAMENTE UMA SENHA:").strip()

                            usuario[i][5] = senha

                            print("\nSENHA ATUALIZADA COM SUCESSO!")
                            break
                        
                        if (achou == False):

                            print("INFORMAÇÕES INCORRETAS! VOLTANDO PARA O MENU...")
                            break

                senha = input("\nINFORME SUA SENHA: ").strip()

                while (senha == ""):

                    print("VALOR INVÁLIDO!")
                    senha = input("\nDIGITE NOVAMENTE: ").strip()

                if (opcao_1 == 'N'):

                    achouUsuario = False

                    for i in range(len(usuario)):

                        if (email == usuario[i][2]) and (senha == usuario[i][5]):

                            logado = True
                            chaveTipo = 1
                            indiceUsuario = i
                            break

                    if (achouUsuario == False):

                        print("\nEMAIL OU SENHA INVÁLIDO!")

                elif (opcao_1 == 'S'):

                    tentativa = 3

                    while tentativa != 0:

                        opcao_2 = input("\nDIGITE A CHAVE DE VERIFICAÇÃO DE ADMINS: ").strip()

                        while (opcao_2 == ""):

                            print("OPÇÃO VAZIA!")
                            opcao_2 = input("\nDIGITE NOVAMENTE: ").strip()

                        if (opcao_2 == chaveSegurancaAdmin):

                            achouAdm = False
        
                            for i in range(len(usuarioAdmin)):

                                if (email == usuarioAdmin[i][2]) and (senha == usuarioAdmin[i][5]):

                                    achouAdm = True

                                    logado = True
                                    chaveTipo = 2
                                    indiceUsuarioAdmin = i
                                    break

                                
                            if (achouAdm == False): 

                                print("\nEMAIL OU SENHA INVÁLIDO!")
                            
                            break

                        else:
                            
                            tentativa -= 1
                            print(f"\nCHAVE INCORRETA! VOCÊ SÓ TEM {tentativa} TENTATIVAS, DIGITE NOVAMENTE!")

                            if ((tentativa == 0) and (logado == False)):

                                print("\nNÃO FOI POSSÍVEL EFETUAR O LOGIN!")
                                break


                if (logado == False):

                    print("--------------------------------------------------------------------------------------------")

                    opcao_3 = input("\nDESEJA TENTAR NOVAMENTE (S/N)? ").strip().upper()

                    while ((opcao_3 not in ['S', 'N'])):

                        print("OPÇÃO INVÁLIDA!")
                        opcao_3 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                    if opcao_3 == 'N':

                        break


                else: 

                    print("\nUSUARIO LOGADO!")

                    break

    elif (opcao_0 == '3'):

        while True:

            if (logado == False):

                print("\n--------------------------------------------------------------------------------------------")
                print("PET-SERVIÇOS E PRODUTOS")

                print("\nPARA CONTINUAR REALIZE O LOGIN!")
                break


            else: 

                if ((chaveTipo == 2) and (logado == True)):

                    print("\n--------------------------------------------------------------------------------------------")
                    print("PET-SERVIÇOS E PRODUTOS")
                    print("ÁREA DO ADMINISTRADOR")
                    print("\nEXPLORE OS MENUS ABAIXO:")
                    print("\n1 - CADASTRAR PRODUTO \n2 - CADASTRAR SERVIÇOS \n3 - ATUALIZAR PRODUTO OU SERVIÇOS \n4 - BUSCAR \n5 - REMOVER PRODUTO OU SERVIÇOS \n6 - HISTÓRICO DE VENDAS E AGENDAMENTO \n0 - VOLTAR PARA O MENU INICIAL")

                    opcao_3 = input("\nDIGITE SUA ESCOLHA: ")

                    if (opcao_3 == '1'):

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("CADASTRO DE PRODUTO")

                            nomeProduto = input("\nDIGITE O NOME DO PRODUTO: ").strip()

                            duplicado = False

                            for i in range(len(produtos)):

                                if (nomeProduto == produtos[i][0]):

                                    duplicado = True
                                    break
                                
                            while (nomeProduto == "" or duplicado == True):

                                print("NOME INVÁLIDO OU JÁ CADASTRADO!")
                                nomeProduto = input("\nINFORME O PRODUTO NOVAMENTE: ").strip()

                                duplicado = False

                                for i in range(len(produtos)):

                                    if (nomeProduto == produtos[i][0]):

                                        duplicado = True
                                        break

                            while True:

                                tipoProduto = input("MENU TIPO DO PRODUTO: \n\n0 - HIGIENE \n1 - ALIMENTAÇÃO \n2 - RECREAÇÃO \n3 - MEDICAMENTOS \n4 - OUTROS \n\nDIGITE A OPÇÃO ESCOLHIDA: ")

                                if (tipoProduto == '0'):

                                    tipoProduto = 'HIGIENE'
                                    break

                                elif (tipoProduto == '1'):

                                    tipoProduto = 'ALIMENTAÇÃO'
                                    break

                                elif (tipoProduto == '2'):

                                    tipoProduto = 'RECREAÇÃO'
                                    break

                                elif (tipoProduto == '3'):

                                    tipoProduto = 'MEDICAMENTOS'
                                    break

                                elif (tipoProduto == '4'):

                                    tipoProduto = 'OUTROS'
                                    break

                                else:

                                    print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!")

                            valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))

                            while (valorProdutos <= 0):

                                print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))

                            quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO NO ESTOQUE: "))

                            while (quantidadeProdutos <= 0):

                                print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO: "))

                            produtos.append([nomeProduto, tipoProduto, valorProdutos, quantidadeProdutos])

                            opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRO PRODUTO (S/N)? ").strip().upper()

                            while ((opcao_2 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_2 == 'N'):

                                print("\nCADASTRO DO(S) PRODUTO(S) REALIZADO!")
                                break
                    
                    elif (opcao_3 == '2'):
                            
                        while True:
                    
                            print("\n--------------------------------------------------------------------------------------------")
                            print("CADASTRO DE SERVIÇOS: ")

                            nomeServicos = input("\nDIGITE O NOME DO SERVIÇO: ").strip()

                            duplicado = False

                            for i in range(len(servicos)):

                                if (nomeServicos == servicos[i][0]):

                                    duplicado = True
                                    break
                                
                            while (nomeServicos == "" or duplicado == True):

                                print("NOME DO SERVIÇO INVÁLIDO OU JÁ CADASTRADO!")
                                nomeServicos = input("\nINFORME O SERVIÇO NOVAMENTE: ").strip()

                                duplicado = False

                                for i in range(len(servicos)):

                                    if (nomeServicos == servicos[i][0]):

                                        duplicado = True
                                        break

                            valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))

                            while (valorServicos <= 0):

                                print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))

                            servicosDatas = []
                            
                            while True:

                                print("\nEXEMPLO: (12/11/2025)")
                                datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ").strip()

                                while (datas == ""):

                                    print("\nDIGITE UMA DATA VÁLIDA!")
                                    print("\nEXEMPLO: (12/11/2025)")
                                    datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ").strip()

                                print("\nEXEMPLO: (08:00/10:00/12:00)")
                                horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NESTA DATA: ").strip()

                                while (horas == "" or '/' not in horas):

                                    print("\nDIGITE UM HORÁRIO VÁLIDO!")
                                    print("\nEXEMPLO: (08:00/10:00/12:00)")
                                    horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NOVAMENTE: ")

                                horasLista = horas.split("/")

                                servicosDatas.append([datas, horasLista])

                                opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRA DATA (S/N)? ").strip().upper()

                                while ((opcao_2 not in ['S', 'N'])):

                                    print("OPÇÃO INVÁLIDA!")
                                    opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                if (opcao_2 == 'N'):

                                    print("\nCADASTRO DA(S) DATA(S) REALIZADO!")
                                    break

                            servicos.append([nomeServicos, valorServicos, servicosDatas])

                            opcao_4 = input("\nDESEJA FAZER O CADASTRO DE OUTRO SERVIÇO (S/N)? ").strip().upper()

                            while ((opcao_4 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_4 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_4 == 'N'):

                                print("\nCADASTRO DO(S) SERVIÇO(S) REALIZADO!")
                                break

                    elif (opcao_3 == '3'):     

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("ATUALIZAR PRODUTOS E SERVIÇOS")

                            opcao_4 = input("\nMENU: \n\n1 - ATUALIZAR PRODUTOS \n2 - ATUALIZAR SERVIÇOS \n0 - VOLTAR PARA O MENU DA ÁREA DO ADMINISTRADOR\n \nDIGITE SUA ESCOLHA: ")

                            if (opcao_4 == '1'):

                                print("\nLISTA DE PRODUTOS:")

                                indice = 0

                                for i in range(len(produtos)):

                                    indice += 1

                                    print(f"\n{indice} - {produtos[i][0]} \nTIPO: {produtos[i][1]} \nVALOR: R${produtos[i][2]} \nQUANTIDADE: {produtos[i][3]}")

                                while True:

                                    opcao_5 = int(input("\nQUAL PRODUTO DESEJA ATUALIZAR? "))

                                    while(opcao_5 > indice):

                                        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                        opcao_5 = int(input("\nQUAL PRODUTO DESEJA REMOVER? "))

                                    opcao_5 -= 1 

                                    valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))

                                    while (valorProdutos <= 0):

                                        print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                        valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))
                                    
                                    produtos[opcao_5][2] = valorProdutos

                                    quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO NO ESTOQUE: "))

                                    while (quantidadeProdutos <= 0):

                                        print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                        quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO: "))
                                    
                                    produtos[opcao_5][3] = quantidadeProdutos

                                    opcao_2 = input("DESEJA ATUALIZAR OUTRO PRODUTO (S/N)? ").strip().upper()

                                    while ((opcao_2 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_2 == 'N'):

                                        print("\nATUALIZAÇÃO(S) REALIZADA!")

                                        break     
                            
                            elif(opcao_4 == '2'):

                                print("\nLISTA DE SERVIÇOS: ")

                                indice = 0

                                for i in range(len(servicos)):

                                    indice += 1

                                    print(f"\n{indice} - {servicos[i][0]} \nVALOR: R${servicos[i][1]}")

                                    for j in range(len(servicos[i][2])):
                                              
                                        print(f"\nDATA(S): {servicos[i][2][j][0]} \nHORÁRIOS(S): {servicos[i][2][j][1]}")

                                while True:

                                    opcao_5 = int(input("\nQUAL SERVIÇO DESEJA ATUALIZAR?"))

                                    while(opcao_5 > indice):

                                        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                        opcao_5 = int(input("\nQUAL PRODUTO DESEJA REMOVER? "))


                                    opcao_5 -= 1 

                                    valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))

                                    while (valorServicos <= 0):

                                        print("\nVALOR ZERADO DIGITE NOVAMENTE!")
                                        valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))
                                    
                                    servicos[opcao_5][1] = valorServicos

                                    servicosDatas = []

                                    while True:

                                        print("\nEXEMPLO: (12/11/2025)")
                                        datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ").strip()

                                        while (datas == ""):

                                            print("\nDIGITE UMA DATA VÁLIDA!")
                                            print("\nEXEMPLO: (12/11/2025)")
                                            datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ").strip()

                                        print("\nEXEMPLO: (08:00/10:00/12:00)")
                                        horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NESTA DATA: ").strip()

                                        while (horas == "" or '/' not in horas):

                                            print("\nDIGITE UM HORÁRIO VÁLIDO!")
                                            print("\nEXEMPLO: (08:00/10:00/12:00)")
                                            horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NOVAMENTE: ")

                                        horasLista = horas.split("/")

                                        servicosDatas.append([datas, horasLista])

                                        opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRA DATA (S/N)? ").strip().upper()

                                        while ((opcao_2 not in ['S', 'N'])):

                                            print("OPÇÃO INVÁLIDA!")
                                            opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                        if (opcao_2 == 'N'):

                                            print("\nCADASTRO DA(S) DATA(S) REALIZADO!")
                                            break

                                    servicos[opcao_5][2] = servicosDatas

                                    opcao_2 = input("\nDESEJA ATUALIZAR OUTRO SERVIÇO (S/N)? ").strip().upper()

                                    while ((opcao_2 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_2 == 'N'):

                                        print("\nATUALIZAÇÃO(S) REALIZADA!")

                                        break     

                            elif(opcao_4 == '0'):

                                break

                            else:
                                print("\nOPÇÃO INVÁLIDA!")

                    elif (opcao_3 == '4'):     

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("BUSCAR PRODUTOS E SERVIÇOS")

                            opcao_4 = input("DIGITE O TIPO DO PRODUTO OU O NOME DO PRODUTO OU SERVIÇO QUE DESEJA BUSCAR: ").strip()

                            while (opcao_4 == ""):

                                print("\nOPÇÃO EM BRANCO DIGITE NOVAMENTE!")
                                opcao_4 = input("DIGITE O TIPO DO PRODUTO OU O NOME DO PRODUTO OU SERVIÇO QUE DESEJA BUSCAR NOVAMENTE: ").strip()

                            buscar_1 = False
                            buscar_2 = False

                            for i in range(len(produtos)):

                                if ((opcao_4 in produtos[i][0]) or (opcao_4 in produtos[i][1])):

                                    print(f"\n{i+1} - {produtos[i][0]} \nTIPO: {produtos[i][1]} \nVALOR: R${produtos[i][2]} \nQUANTIDADE: {produtos[i][3]}")

                                else:

                                    buscar_1 = True

                            for i in range(len(servicos)):
                                    
                                if (opcao_4 in servicos[i][0]):

                                    print(f"\n{i+1} - {servicos[i][0]} \nVALOR: R${servicos[i][1]}")

                                    for j in range(len(servicos[i][2])):
                                              
                                        print(f"\nDATA(S): {servicos[i][2][j][0]} \nHORÁRIO(S): {servicos[i][2][j][1]}")

                                else: 

                                    buscar_2 = True

                            if ((buscar_1 == True) and (buscar_2 == True)):

                                print("\nNÃO LOCALIZAMOS NENHUM PRODUTO OU SERVIÇO. TENTE NOVAMENTE!")

                            elif (buscar_1 == True):

                                print("\nNÃO LOCALIZAMOS UM PRODUTO!")

                            elif (buscar_2 == True):

                                print("\nNÃO LOCALIZADO UM SERVIÇO!")

                            opcao_2 = input("DESEJA BUSCAR OUTRO PRODUTO OU SERVIÇO (S/N)? ").strip().upper()

                            while ((opcao_2 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_2 == 'N'):

                                break     

                    elif (opcao_3 == '5'):     

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("REMOVER PRODUTOS E SERVIÇOS")

                            opcao_4 = input("\nMENU: \n\n1 - REMOVER PRODUTOS \n2 - REMOVER SERVIÇOS \n0 - VOLTAR PARA O MENU DA ÁREA DO ADMINISTRADOR\n \nDIGITE SUA ESCOLHA: ")

                            if (opcao_4 == '1'):

                                print("\nLISTA DE PRODUTOS:")

                                indice = 0

                                for i in range(len(produtos)):

                                    indice += 1

                                    print(f"\n{indice} - {produtos[i][0]} \nTIPO: {produtos[i][1]} \nVALOR: R${produtos[i][2]} \nQUANTIDADE: {produtos[i][3]}")

                                while True:

                                    opcao_5 = int(input("\nQUAL PRODUTO DESEJA REMOVER? "))

                                    while(opcao_5 > indice):

                                        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                        opcao_5 = int(input("\nQUAL PRODUTO DESEJA REMOVER? "))

                                    opcao_5 -= 1 

                                    produtos.remove(produtos[opcao_5])

                                    opcao_2 = input("DESEJA REMOVER OUTRO PRODUTO (S/N)? ").strip().upper()

                                    while ((opcao_2 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_2 == 'N'):

                                        print("\nREMOÇÃO(ÕES) REALIZADA!")

                                        break     
                            
                            elif(opcao_4 == '2'):

                                print("\nLISTA DE SERVIÇOS:")

                                indice = 0

                                for i in range(len(servicos)):

                                    indice += 1

                                    print(f"\n{indice} - {servicos[i][0]} \nVALOR: R${servicos[i][1]}")

                                    for j in range(len(servicos[i][2])):
                                              
                                        print(f"\nDATA(S): {servicos[i][2][j][0]} \nHORÁRIOS(S): {servicos[i][2][j][1]}")

                                while True:

                                    opcao_5 = int(input("\nQUAL SERVIÇO DESEJA REMOVER?"))

                                    while(opcao_5 > indice):

                                        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                        opcao_5 = int(input("\nQUAL PRODUTO DESEJA REMOVER? "))


                                    opcao_5 -= 1 

                                    servicos.remove(servicos[opcao_5])

                                    opcao_2 = input("\nDESEJA REMOVER OUTRO SERVIÇO (S/N)? ").strip().upper()

                                    while ((opcao_2 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_2 == 'N'):

                                        print("\nREMOÇÃO(ÕES) REALIZADA!")

                                        break     

                            elif(opcao_4 == '0'):

                                break

                            else:
                                print("\nOPÇÃO INVÁLIDA!")

                    elif (opcao_6 == '6'):

                        print("\n--------------------------------------------------------------------------------------------")
                        print("HISTÓRICO DE VENDAS E AGENDAMENTOS")

                        if (len(encomendas) == 0):

                            print("\nNENHUMA VENDA REGISTRADA!")

                        else:

                            indice = 0

                            for i in range(len(encomendas)):

                                indice += 1

                                print(f"\n{indice} - PRODUTO: {encomendas[i][0]} \nQUANTIDADE: {encomendas[i][1]}")
                                print(f"VALOR TOTAL: R${encomendas[i][2]:.2f} \nCLIENTE: {encomendas[i][3][0]}")

                        if len(agendamentos) == 0:
                            
                            print("\nNENHUM AGENDAMENTO REGISTRADO!.")

                        else:

                            indice = 0

                            for i in range(len(agendamentos)):

                                indice += 1

                                print(f"\n{indice} - SERVIÇO: {agendamentos[i][0][0]} \nDATA: {agendamentos[i][1]}")
                                print(f"HORÁRIO: {agendamentos[i][2]} \nCLIENTE: {agendamentos[i][3][0]}")

                    elif (opcao_3 == '0'):

                        print("\nVOLTANDO PARA O MENU INICIAL...")

                    else:

                        print("\nOPÇÃO INVÁLIDA!")

                elif((chaveTipo == 1) and (logado == True)):

                    print("\n--------------------------------------------------------------------------------------------")
                    print("PET-SERVIÇOS E PRODUTOS")
                    print("ÁREA DO USUÁRIO")
                    print("\nEXPLORE OS MENUS ABAIXO:")
                    print("\n1 - COMPRAR PRODUTO \n2 - AGENDAR SERVIÇOS \n3 - BUSCAR \n4 - PETS \n0 - VOLTAR PARA O MENU INICIAL")

                    opcao_3 = input("\nDIGITE SUA ESCOLHA: ")

                    if (opcao_3 == '1'):

                        print("\n--------------------------------------------------------------------------------------------")
                        print("\nCOMPRA DE PRODUTOS: ")

                        print("\nLISTA DE PRODUTOS: ")

                        indice = 0

                        for i in range(len(produtos)):

                            indice += 1

                            print(f"\n{indice} - {produtos[i][0]} \nTIPO: {produtos[i][1]} \nVALOR: R${produtos[i][2]} \nQUANTIDADE: {produtos[i][3]}")

                        valorTotal = 0

                        while True:

                            opcao_5 = int(input("\nDIGITE O ÍNDICE DO PRODUTO QUE DESEJA COMPRAR: "))

                            while((opcao_5 <= 0) or (opcao_5 > indice)):

                                print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                opcao_5 = int(input("\nDIGITE NOVAMENTE O ÍNDICE: "))

                            opcao_5 -= 1 

                            quantidade = int(input("\nDIGITE A QUANTIDADE QUE VOCÊ DESEJA COMPRAR: "))

                            if (quantidade <= produtos[opcao_5][3]):

                                valorTotal = quantidade * produtos[opcao_5][2]

                                opcao_8 = input(f"\nDESEJA CONFIRMAR O PEDIDO, NO VALOR DE R${valorTotal} (S/N)? ").strip().upper()

                                while ((opcao_8 not in ['S', 'N'])):

                                    print("OPÇÃO INVÁLIDA!")
                                    opcao_8 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                if (opcao_8 == 'N'):

                                    print("\nVOLTANDO PARA O MENU DE USUARIO...")

                                    break

                                else:

                                    produtos[opcao_5][3] -= quantidade

                                    encomendas.append([produtos[opcao_5], quantidade, valorTotal, usuario[indiceUsuario]])
                             
                            else:

                                print("\nQUANTIDADE INDISPONÍVEL EM ESTOQUE!")

                            opcao_2 = input("DESEJA ENCOMENDAR OUTRO PRODUTO (S/N)? ").strip().upper()

                            while ((opcao_2 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_2 == 'N'):

                                print(f"\nSUA COMPRA FOI COMPUTADORIZADA, O TOTAL DA COMPRA FOI DE R${valorTotal} O PAGAMENTO É FEITO DIRETAMENTE NO PETSHOP!")

                                break     

                    elif (opcao_3 == '2'):

                        print("\n--------------------------------------------------------------------------------------------")
                        print("\nAGENDAMENTO DE SERVIÇOS: ")

                        print("\nLISTA DE SERVIÇOS: ")

                        indice = 0

                        for i in range(len(servicos)):

                                    indice += 1

                                    print(f"\n{indice} - {servicos[i][0]} \nVALOR: R${servicos[i][1]}")

                                    for j in range(len(servicos[i][2])):
                                              
                                        print(f"\nDATA(S): {servicos[i][2][j][0]} \nHORÁRIOS(S): {servicos[i][2][j][1]}")

                        valorTotal = 0

                        while True:

                            opcao_5 = int(input("\nDIGITE O ÍNDICE DO SERVIÇO QUE DESEJA AGENDAR? "))

                            while((opcao_5 <= 0) or (opcao_5 > indice)):

                                print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                opcao_5 = int(input("\nDIGITE NOVAMENTE O ÍNDICE DO SERVIÇO QUE DESEJA AGENDAR? "))

                            opcao_5 -= 1 

                            data = input("\nDIGITE QUE DATA VOCÊ DESEJA AGENDAR: ")
                            marcadoData = ''

                            hora = input("\nDIGITE QUE HORÁRIO VOCÊ DESEJA AGENDAR: ")
                            marcadoHora = ''
                            indiceHora = 0
                            ii = 0
                            jj = 0

                            for i in range(len(servicos)):
                                    
                                    for j in range(len(servicos[i][2])):

                                        if (data == servicos[i][2][j][0]):

                                            marcadoData = servicos[i][2][j][0]

                                            for k in range(len(servicos[i][2][j][1])):

                                                if (hora == servicos[i][2][j][1][k]):

                                                    marcadoHora = servicos[i][2][j][1][k]
                                                    ii = i
                                                    jj = j
                                                    indiceHora = k
                                              
                            valorTotal += servicos[opcao_5][1]

                            opcao_7 = input(f"\nDESEJA CONFIRMAR O SERVIÇO, PARA A DATA: {marcadoData} E HORÁRIO: {marcadoHora} NO VALOR DE R${valorTotal} (S/N)? ").strip().upper()

                            while ((opcao_7 not in ['S', 'N'])):

                                print("OPÇÃO INVÁLIDA!")
                                opcao_7 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                            if (opcao_7 == 'N'):

                                print("\nVOLTANDO PARA O MENU DE USUARIO...")

                                break

                            else:

                                marcadoHora = servicos[ii][2][jj][1].pop(indiceHora)

                                agendamentos.append([servicos[opcao_5], marcadoData, marcadoHora, usuario[indiceUsuario]])

                                opcao_2 = input("\nDESEJA AGENDAR OUTRO SERVIÇO (S/N)? ").strip().upper()

                                while ((opcao_2 not in ['S', 'N'])):

                                    print("OPÇÃO INVÁLIDA!")
                                    opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                if (opcao_2 == 'N'):

                                    print(f"\nSEU(S) AGENDAMENTO(S) FOI COMPUTADORIZADO(S), O VALOR DO SERVIÇO FOI DE R${valorTotal} O PAGAMENTO É FEITO DIRETAMENTE NO PETSHOP!")

                                    break
                    
                    elif(opcao_3 == '3'):

                        while True:

                            print("\n--------------------------------------------------------------------------------------------")
                            print("BUSCAR PRODUTOS E SERVIÇOS")

                            opcao_5 = input("\nMENUS: \n\n1 - PRODUTOS \n2 - SERVIÇOS \n3 - VOLTAR PARA A ÁREA DO USUÁRIO \n\nDIGITE SUA ESCOLHA: ")

                            if (opcao_5 == '1'):

                                opcao_4 = input("\nDIGITE O NOME OU TIPO DO PRODUTO QUE DESEJA BUSCAR: ").strip()

                                while (opcao_4 == ""):

                                    print("\nOPÇÃO EM BRANCO DIGITE NOVAMENTE!")
                                    opcao_4 = input("DIGITE O NOME OU TIPO DO PRODUTO QUE DESEJA BUSCAR NOVAMENTE: ").strip()

                                buscar_1 = False

                                for i in range(len(produtos)):

                                    if ((opcao_4 in produtos[i][0]) or (opcao_4 in produtos[i][1])):

                                        print(f"\n{i+1} - {produtos[i][0]} \nTIPO: {produtos[i][1]} \nVALOR: R${produtos[i][2]} \nQUANTIDADE: {produtos[i][3]}")

                                    else:

                                        buscar_1 = True

                                if (buscar_1 == True):

                                    print("\nNÃO LOCALIZAMOS O PRODUTO!")

                                else:

                                    opcao_6 = input("\nDESEJA COMPRAR O PRODUTO (S/N)? ").strip().upper()

                                    while ((opcao_6 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_6 == 'S'):

                                        opcao_7 = int(input("\nDIGITE O ÍNDICE DO PRODUTO QUE DESEJA COMPRAR: "))

                                        while((opcao_7 <= 0) or (opcao_7 > indice)):

                                            print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                            opcao_7 = int(input("\nDIGITE NOVAMENTE O ÍNDICE: "))

                                        opcao_7 -= 1 

                                        if (quantidade <= produtos[opcao_5][3]):

                                            valorTotal = quantidade * produtos[opcao_5][2]

                                            opcao_8 = input(f"\nDESEJA CONFIRMAR O PEDIDO, NO VALOR DE R${valorTotal} (S/N)? ").strip().upper()

                                            while ((opcao_8 not in ['S', 'N'])):

                                                print("OPÇÃO INVÁLIDA!")
                                                opcao_8 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                            if (opcao_8 == 'N'):

                                                print("\nVOLTANDO PARA O MENU DE USUARIO...")

                                                break

                                            else:

                                                produtos[opcao_7][3] -= quantidade

                                                encomendas.append([produtos[opcao_7], quantidade, valorTotal, usuario[indiceUsuario]])

                                                print(f"\nSUA COMPRA FOI COMPUTADORIZADA, O TOTAL DA COMPRA FOI DE R${valorTotal} O PAGAMENTO É FEITO DIRETAMENTE NO PETSHOP!")
                                            
                                        else:

                                            print("\nQUANTIDADE INDISPONÍVEL EM ESTOQUE!")

                                    else:

                                        print("\nVOLTANDO PARA O MENU DE BUSCA...")
                            
                            elif(opcao_5 == '2'):

                                opcao_4 = input("\nDIGITE O NOME DO SERVIÇO QUE DESEJA BUSCAR: ").strip()

                                while (opcao_4 == ""):

                                    print("\nOPÇÃO EM BRANCO DIGITE NOVAMENTE!")
                                    opcao_4 = input("DIGITE O NOME DO SERVIÇO QUE DESEJA BUSCAR NOVAMENTE: ").strip()

                                buscar_2 = False

                                for i in range(len(servicos)):
                                        
                                    if (opcao_4 in servicos[i][0]):

                                        print(f"\n{i+1} - {servicos[i][0]} \nVALOR: R${servicos[i][1]}")

                                        for j in range(len(servicos[i][2])):
                                                
                                            print(f"\nDATA(S): {servicos[i][2][j][0]} \nHORÁRIO(S): {servicos[i][2][j][1]}")

                                    else: 

                                        buscar_2 = True
                                    
                                if (buscar_2 == True):

                                    print("\nNÃO LOCALIZADO O SERVIÇO!")
                                
                                else:

                                    opcao_6 = input("\nDESEJA AGENDAR O SERVIÇO (S/N)? ").strip().upper()

                                    while ((opcao_6 not in ['S', 'N'])):

                                        print("OPÇÃO INVÁLIDA!")
                                        opcao_6 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                    if (opcao_6 == 'S'):

                                        opcao_7 = int(input("\nDIGITE O ÍNDICE DO SERVIÇO QUE DESEJA AGENDAR? "))

                                        while((opcao_7 <= 0) or (opcao_7 > indice)):

                                            print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                            opcao_7 = int(input("\nQUAL PRODUTO DESEJA ENCOMENDAR? "))

                                        opcao_7 -= 1 

                                        data = input("\nDIGITE QUE DATA VOCÊ DESEJA AGENDAR: ")
                                        marcadoData = ''

                                        hora = input("\nDIGITE QUE HORÁRIO VOCÊ DESEJA AGENDAR: ")
                                        marcadoHora = ''
                                        indiceHora = 0

                                        for i in range(len(servicos)):
                                                
                                                for j in range(len(servicos[i][2])):

                                                    if (data == servicos[i][2][j][0]):

                                                        marcadoData = servicos[i][2][j][0]

                                                        for k in range(len(servicos[i][2][j][1])):

                                                            if (hora == servicos[i][2][j][1][k]):

                                                                marcadoHora = servicos[i][2][j][1][k]
                                                                indiceHora = k
                                                        
                                        valorTotal += servicos[opcao_5][1]

                                        opcao_7 = input(f"\nDESEJA CONFIRMAR O SERVIÇO, PARA A DATA: {marcadoData} E HORÁRIO: {marcadoHora} NO VALOR DE R${valorTotal} (S/N)? ").strip().upper()

                                        while ((opcao_7 not in ['S', 'N'])):

                                            print("OPÇÃO INVÁLIDA!")
                                            opcao_7 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                        if (opcao_7 == 'N'):

                                            print("\nVOLTANDO PARA O MENU DE BUSCA...")

                                        else:

                                            marcadoHora = servicos[i][2][j][1].pop(indiceHora)

                                            agendamentos.append([servicos[opcao_5], marcadoData, marcadoHora, usuario[indiceUsuario]])

                                            print(f"\nSEU(S) AGENDAMENTO(S) FOI COMPUTADORIZADO(S), O VALOR DO SERVIÇO FOI DE R${valorTotal} O PAGAMENTO É FEITO DIRETAMENTE NO PETSHOP!")

                            elif (opcao_5 == '3'):

                                print("\nVOLTANDO PARA O MENU DE USUÁRIO...")
                                break

                    elif(opcao_3 == '4'):

                        while True:

                            if ((len(usuario[indiceUsuario]) > 7) and (usuario[indiceUsuario][7] != [])):

                                while True:

                                    print("\n--------------------------------------------------------------------------------------------")
                                    print("PETS")

                                    print("\nPET CADASTRADOS: ")
                                    indice = 0

                                    for i in range(len(usuario[indiceUsuario][7])):

                                        indice += 1

                                        print(f"\n{indice} - {usuario[indiceUsuario][7][i][1]} \nTIPO: {usuario[indiceUsuario][7][i][0]} | RAÇA: {usuario[indiceUsuario][7][i][2]}")
                                        print(f"\nIDADE: {usuario[indiceUsuario][7][i][3]} | PESO: {usuario[indiceUsuario][7][i][4]} \nANIMAL COM VACINA EM DIA? {usuario[indiceUsuario][7][i][5]}")

                                    opcao_4 = input("\nMENU: \n\n1 - ADICIONAR \n2 - REMOVER \n0 - VOLTAR PARA O MENU DE USUÁRIO \n\nDIGITE SUA ESCOLHA:")

                                    if (opcao_4 == '1'):

                                        petUsuario = []

                                        while True:

                                            print("\n--------------------------------------------------------------------------------------------")
                                            print("CADASTRO DE PETS")

                                            tipoPet = input("\nQUAL TIPO DE ANIMAL É O SEU PET? ").strip()

                                            while (tipoPet == ""):

                                                print("OPÇÃO VAZIA!")
                                                tipoPet = input("\nDIGITE NOVAMENTE: ").strip()
                                        
                                            nomePet = input("\nINFORME O NOME DO SEU PET: ").strip()

                                            while (nomePet == ""):

                                                print("NOME INVÁLIDO")
                                                nomePet = input("\nINFORME O NOME NOVAMENTE: ").strip()

                                            racaPet = input("\nINFORME A RAÇA DO SEU PET (SE NÃO HOUVER DIGITE 'RND'): ").strip()

                                            while (racaPet == ""):

                                                print("RAÇA INVÁLIDA")
                                                racaPet = input("\nINFORME A RAÇA NOVAMENTE: ").strip()

                                            idadePet = input("\nINFORME A IDADE DO SEU PET: ").strip()

                                            while (idadePet == ""):

                                                print("IDADE INVÁLIDA!")
                                                idadePet = input("\nINFORME A IDADE NOVAMENTE: ").strip()
                                        
                                            pesoPet = input("\nINFORME O PESO DO SEU PET: ").strip()

                                            while (pesoPet == ""):

                                                print("PESO INVÁLIDO!")
                                                pesoPet = input("\nINFORME O PESO NOVAMENTE: ").strip()

                                            vacina = input("\nAS VACINAS DO SEU PET ESTÃO EM DIA (S/N)? ").strip().upper()

                                            while ((vacina not in ['S', 'N'])):

                                                print("OPÇÃO INVÁLIDA!")
                                                vacina = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                            petUsuario.append([tipoPet, nomePet, racaPet, idadePet, pesoPet, vacina])

                                            opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRO ANIMAL (S/N)? ").strip().upper()

                                            while ((opcao_2 not in ['S', 'N'])):

                                                print("OPÇÃO INVÁLIDA!")
                                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                            if (opcao_2 == 'N'):

                                                print("\nCADASTRO(S) DO(S) PET(S) REALIZADO!")

                                                break     
                                    
                                        usuario[-1].append(petUsuario)
                                        break
                                    
                                    elif (opcao_4 == '2'):

                                        while True:

                                            opcao_5 = int(input("\nQUAL O INDICE DO ANIMAL QUE VOCÊ DESEJA REMOVER? "))

                                            while(opcao_5 > indice):

                                                print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                                opcao_5 = int(input("\nQUAL ANIMAL DESEJA REMOVER? "))

                                            opcao_5 -= 1 

                                            usuario[indiceUsuario][7].pop(opcao_5)

                                            opcao_2 = input("DESEJA REMOVER OUTRO PRODUTO (S/N)? ").strip().upper()

                                            while ((opcao_2 not in ['S', 'N'])):

                                                print("OPÇÃO INVÁLIDA!")
                                                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                            if (opcao_2 == 'N'):

                                                print("\nREMOÇÃO(ÕES) REALIZADA!")

                                                break     
                                    
                                    elif (opcao_4 == '0'):

                                        print("\nVOLTANDO PARA O MENU DE USUÁRIO...")
                                        break

                                    else:

                                        print("\n OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
                                
                                break

                            else:

                                print("\nNENHUM ANIMAL CADASTRADO!")

                                opcao_1 = input("\nDESEJA REALIZAR O CADASTRO DO SEU PET (S/N)? ").strip().upper()

                                while ((opcao_1 not in ['S', 'N'])):

                                    print("OPÇÃO INVÁLIDA!")
                                    opcao_1 = input("\nDIGITE NOVAMENTE: ").strip().upper()
                                
                                if (opcao_1 == 'S'):

                                    petUsuario = []

                                    while True:

                                        print("\n--------------------------------------------------------------------------------------------")
                                        print("CADASTRO DE PETS")

                                        tipoPet = input("\nQUAL TIPO DE ANIMAL É O SEU PET? ").strip()

                                        while (tipoPet == ""):

                                            print("OPÇÃO VAZIA!")
                                            tipoPet = input("\nDIGITE NOVAMENTE: ").strip()
                                    
                                        nomePet = input("\nINFORME O NOME DO SEU PET: ").strip()

                                        while (nomePet == ""):

                                            print("NOME INVÁLIDO")
                                            nomePet = input("\nINFORME O NOME NOVAMENTE: ").strip()

                                        racaPet = input("\nINFORME A RAÇA DO SEU PET (SE NÃO HOUVER DIGITE 'RND'): ").strip()

                                        while (racaPet == ""):

                                            print("RAÇA INVÁLIDA")
                                            racaPet = input("\nINFORME A RAÇA NOVAMENTE: ").strip()

                                        idadePet = input("\nINFORME A IDADE DO SEU PET: ").strip()

                                        while (idadePet == ""):

                                            print("IDADE INVÁLIDA!")
                                            idadePet = input("\nINFORME A IDADE NOVAMENTE: ").strip()
                                    
                                        pesoPet = input("\nINFORME O PESO DO SEU PET: ").strip()

                                        while (pesoPet == ""):

                                            print("PESO INVÁLIDO!")
                                            pesoPet = input("\nINFORME O PESO NOVAMENTE: ").strip()

                                        vacina = input("\nAS VACINAS DO SEU PET ESTÃO EM DIA (S/N)? ").strip().upper()

                                        while ((vacina not in ['S', 'N'])):

                                            print("OPÇÃO INVÁLIDA!")
                                            vacina = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                        petUsuario.append([tipoPet, nomePet, racaPet, idadePet, pesoPet, vacina])

                                        opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRO ANIMAL (S/N)? ").strip().upper()

                                        while ((opcao_2 not in ['S', 'N'])):

                                            print("OPÇÃO INVÁLIDA!")
                                            opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()

                                        if (opcao_2 == 'N'):

                                            print("\nCADASTRO(S) DO(S) PET(S) REALIZADO!")

                                            break     
                                
                                    usuario[-1].append(petUsuario)
                                    break
                                
                                else:

                                    print("\nVOLTANDO PARA O MENU DE USUÁRIO...")
                                
                                break


                    elif (opcao_3 == '0'):

                        print("\nVOLTANDO PARA A ÁREA DO USUÁRIO...")
                        break

                    else:

                        ("\nOPÇÃO INVÁLIDA TENTE NOVAMENTE!")

    elif (opcao_0 == '4'):

        while True:

            print("--------------------------------------------------------------------------------------------")
            print("DESLOGAR USUÁRIO:")

            opcao_2 = input("\nDESEJA REALMENTE SAIR DA CONTA (S/N)? ").strip().upper()

            while ((opcao_2 not in ['S', 'N'])):

                print("OPÇÃO INVÁLIDA!")
                opcao_2 = input("\nDIGITE NOVAMENTE: ").strip().upper()
            
            if opcao_2 == 'S':

                print("\nUSUARIO DESLOGADO!")
                logado = False
                chaveTipo = 0
                indiceUsuario = 0
                indiceUsuarioAdmin = 0
                break
            
            else:

                break

    elif (opcao_0 == '0'):

        print("\nSISTEMA ENCERRADO!")
        break   

    else: 
        
        print("\nVALOR INVÁLIDO TENTE NOVAMENTE")