from modulos import validacao
import datetime

rota = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\usuarios.txt"
rota1 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\pets.txt"
rota2 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\produtos.txt"
rota3 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\servicos.txt"
rota4 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\vendas.txt"
rota5 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\agendamento.txt"


def salvarCliente(nome, CPF, email, numero, idade, senha, verificacao, logado, tipoUsuario, idPet):

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota, "a") as arquivo:

        arquivo.write(f"{nome};{CPF};{email};{numero};{idade};{senha};{verificacao};{logado};{tipoUsuario};{idPet}\n")

    return None

def atualizarCliente(idPet, usuario):
    
    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

    localizado = False

    with open(rota, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (usuario['nome'] == sublista[0]):

               pets = sublista[9] + idPet

               sublista[9] = pets.split("-")

               arquivo.write(f"{sublista[0]};{sublista[1]};{sublista[2]};{sublista[3]};{sublista[4]};{sublista[5]};{sublista[6]};{sublista[7]};{sublista[8]};{sublista[9]}\n")

            else:

                arquivo.write(linha)



    if localizado:

        print("\nSTATUS DE LOGIN/LOGOUT ATUALIZADO COM SUCESSO!")

    else:
    
        print("\nUSUÁRIO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def salvarColaborador(nome, CPF, email, numero, idade, senha, verificacao, logado, tipoUsuario):

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()
        
    with open(rota, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota, "a") as arquivo:

        arquivo.write(f"{nome};{CPF};{email};{numero};{idade};{senha};{verificacao};{logado};{tipoUsuario}\n")

    return None

def salvarPet(idPet, nome, tipo, idadePet, raca):

    with open(rota1, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota1, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota1, "a") as arquivo:

        arquivo.write(f"{idPet};{nome};{tipo};{idadePet};{raca}\n")

    return None

def acessarPet():

    pets = []

    with open(rota1, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas: 

            sublista = linha.split(";")

            pet = {

                'idPet': sublista[0],
                'nome': sublista[1],
                'tipo': sublista[2],
                'idade': sublista[3],
                'raca': sublista[4]

            }

            pets.append(pet)

    return pet

def atualizarLoginLogout(logado, email, senha):

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

    localizado = False

    with open(rota, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (email == sublista[2] and senha == sublista[5]):

                linhaAtualizada = ""

                localizado = 0

                for i in range(len(sublista)):

                    if i == 7:

                        linhaAtualizada += f"{logado};"

                    else:

                        linhaAtualizada += f"{sublista[i]};"

                linhaAtualizada = linhaAtualizada[:-1]

                arquivo.write(f"{linhaAtualizada}\n")

                localizado = True

            else:

                arquivo.write(linha)



    if localizado:

        print("\nSTATUS DE LOGIN/LOGOUT ATUALIZADO COM SUCESSO!")

    else:
    
        print("\nUSUÁRIO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def resetarUsuariosLogados():

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            linhaAtualizada = ""

            for i in range(len(sublista)):

                if i == 7:

                    linhaAtualizada += "False;"

                else:

                    linhaAtualizada += f"{sublista[i]};"

            linhaAtualizada = linhaAtualizada[:-1]

            arquivo.write(f"{linhaAtualizada}\n")

    return None

def salvarProdutos(nomeProdutos, tipoProduto, valorProdutos, quantidadeProdutos, validadeProdutos):

    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()
        
    with open(rota2, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota2, "a") as arquivo:

        arquivo.write(f"{nomeProdutos};{tipoProduto};{valorProdutos};{quantidadeProdutos};{validadeProdutos}\n")

    return None

def acessarProdutos():

    produtos = []

    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas: 

            sublista = linha.split(";")

            produto = {

                'nome': sublista[0],
                'tipo': sublista[1],
                'valor': sublista[2],
                'quantidade': sublista[3],
                'validade': sublista[4]

            }

            produtos.append(produto)

    return produtos

def salvarServicos(nomeServico, valorServico, dataServico):
    
    with open(rota3, "r") as arquivo:

        linhas = arquivo.readlines()
        
    with open(rota3, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota3, "a") as arquivo:

        linha = f"{nomeServico};{valorServico};"

        contagemData = 0

    totalDatas = len(dataServico)

    for data in dataServico:

        linha += data + ":"

        horarios = dataServico[data]

        for i in range(len(horarios)):

            linha += horarios[i]

            if i < len(horarios) - 1:

                linha += ","

        contagemData += 1

        if contagemData < totalDatas:

            linha += "|"

    linha += "\n"

    with open(rota3, "a") as arquivo:

        arquivo.write(linha)

    return None

def acessarServicos():

    servicos = []

    with open(rota3, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas: 

            sublista = linha.split(";")

            servicosDatas = {}

            datasSeparadas = sublista[2].split("|")

            for i in range(len(datasSeparadas)):

                item = datasSeparadas[i]

                data = item.split(":", 1)[0]
                
                horariosStr = item.split(":", 1)[1]

                horarios = horariosStr.split(",")

                servicosDatas[data] = horarios

            servico = {

                'nome': sublista[0],
                'valor': sublista[1],
                'datas': servicosDatas

            }

            servicos.append(servico)

    return servicos

def salvarVendas(usuario, nomeProdutoAcao, quantidade, valorTotal):

    with open(rota4, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota4, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)
        
    with open(rota4, "a") as arquivo:

        arquivo.write(f"{usuario['nome']};{nomeProdutoAcao};{quantidade};{valorTotal}\n")

def salvarAgendamentos(usuario, nomeServico, valorServico, data, horario):

    with open(rota5, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota5, "w") as arquivo:

        for linha in linhas:

            arquivo.write(linha)

    with open(rota5, "a") as arquivo:
        linha = f"{usuario};{nomeServico};{valorServico};{data};{horario}\n"
        arquivo.write(linha)

def removerPet():

    idPet = input("\nDIGITE O ID DO PET QUE DESEJA REMOVER: ")

    while not validacao.verificaVazio(idPet):

        idPet = input("\nDIGITE O ID DO PET QUE DESEJA REMOVER: ")

    with open(rota1, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota1, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            localizado = 0

            if (idPet == sublista[0]):

                localizado = True

            else:

                arquivo.write(linha)

    if localizado:

        print("\nPET REMOVIDO COM SUCESSO!")

    else:

        print("\nPET NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def removerProduto(nomeProduto):

    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota2, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            localizado = 0

            if (nomeProduto == sublista[0]):

                localizado = True

            else:

                arquivo.write(linha)

    if localizado:

        print("\nPRODUTO REMOVIDO COM SUCESSO!")

    else:

        print("\nPRODUTO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def removerServico(nomeServico):

    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()

    with open(rota2, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            localizado = 0

            if (nomeServico == sublista[0]):

                localizado = True

            else:

                arquivo.write(linha)

    if localizado:

        print("\nPRODUTO REMOVIDO COM SUCESSO!")

    else:

        print("\nPRODUTO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def atualizarServico(nomeServicoAcao, nomeServico, valorServico, dataServico):

    localizado = False
    
    with open(rota3, "r") as arquivo:

        linhas = arquivo.readlines()

    localizado = False

    with open(rota3, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (nomeServicoAcao == sublista[0]):

                linha = f"{nomeServico};{valorServico};{dataServico}\n"

                arquivo.write(linha)

                localizado = True

            else:

                arquivo.write(linha)

    if localizado:

        print("\nSERVIÇO ATUALIZADO COM SUCESSO!")

    else:
    
        print("\nSERVIÇO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def atualizarProduto(nomeProdutoAcao, nomeProduto, tipoProduto, valorProduto, quantidadeProduto, validadeProduto):

    localizado = False
    
    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()

    localizado = False

    with open(rota2, "w") as arquivo:

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (nomeProdutoAcao == sublista[0]):

                linha = f"{nomeProduto};{valorProduto};{tipoProduto};{valorProduto};{quantidadeProduto};{validadeProduto}\n"

                arquivo.write(linha)

                localizado = True

            else:

                arquivo.write(linha)

    if localizado:

        print("\nPRODUTO ATUALIZADO COM SUCESSO!")

    else:
    
        print("\nPRODUTO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
    
    return None

def busca():

    buscaAcao = input("\nDIGITE O NOME DO PRODUTO OU SERVICO QUE VOCÊ DESEJA BUSCAR: ").lower()
    buscaAcao = buscaAcao.lower()

    servico = acessarServicos()
    produto = acessarProdutos()

    for servicoo in servico:

        if buscaAcao in (servicoo['nome'].lower()):

            print(f"\nNOME: {servico['nome']} | VALOR: R${servico['valor']}")

            for data in servico['datas']:

                horarios = servico['datas'][data]

                print(f"\nDATA: {data}")
                print("HORÁRIOS:")

                for i in range(len(horarios)):

                    print("-", horarios[i])

    for produtoo in produto:

        if buscaAcao in (produtoo['nome'].ower()):

            print(f"\nNOME: {produtoo['nome']} | VALIDADE: {produtoo['validade']}"  \
                f"\nVALOR: {produtoo['valor']} | QUANTIDE: {produtoo['quantidade']}" \
                f"\nTIPO: {produtoo['tipo']}")

def realizarCompra(nomeProdutoAcao, quantidade, usuario):

    produto = acessarProdutos()

    valorTotal = 0

    for produtoo in produto:

        if nomeProdutoAcao in (produtoo['nome']):

            valorTotal = float(produtoo['valor']) * quantidade

            opcao = input(f"\nDESEJA FINALIZAR SUA COMPRA NO VALOR DE R${valorTotal} (S/N)? ")

            while not validacao.verificaBoolean(opcao):

                opcao = input(f"\nDESEJA FINALIZAR SUA COMPRA NO VALOR DE R${valorTotal} (S/N)? ")

            if opcao.lower() == 's':

                with open(rota2, "r") as arquivo:

                    linhas = arquivo.readlines()

                localizado = False

                with open(rota2, "w") as arquivo:

                    for linha in linhas:

                        sublista = linha.strip().split(";")

                        if (nomeProdutoAcao == sublista[0]):

                            linha = f"{sublista[0]};{sublista[1]};{sublista[2]};{int(sublista[3])-quantidade};{sublista[4]}\n"

                            arquivo.write(linha)

                            localizado = True

                        else:

                            arquivo.write(linha)

                if localizado:

                    print("\nPRODUTO ATUALIZADO COM SUCESSO!")

                else:
                
                    print("\nPRODUTO NÃO ENCONTRADO! POR FAVOR, TENTE NOVAMENTE.")
                    return

            salvarVendas(usuario, nomeProdutoAcao, quantidade, valorTotal)
                
    return None

def realizarAgedamento(servicos):

    with open(rota3, "w") as arquivo:

        for servico in servicos:

            linha = servico['nome'] + ";" + servico['valor'] + ";"

            datas = servico['datas']

            contador_data = 0

            for data in datas:

                linha += data + ":"

                horarios = datas[data]

                contador_horario = 0

                for horario in horarios:

                    linha += horario

                    contador_horario += 1

                    if contador_horario < len(horarios):

                        linha += ","

                contador_data += 1

                if contador_data < len(datas):

                    linha += "|"

            linha += "\n"

            arquivo.write(linha)

def acessarCompras():

    compras = []

    with open(rota4, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas: 

            sublista = linha.split(";")

            compra = {

                'nomeUsuario': sublista[0],
                'nomeProduto': sublista[1],
                'quantidade': sublista[2],
                'valorTotal': sublista[3]

            }
            compras.append(compra)

    return compras

def acessarAgendamentos():

    agendamentos = []

    with open(rota5, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas: 

            sublista = linha.split(";")

            agendas = {

                'nomeUsuario': sublista[0],
                'nomeServios': sublista[1],
                'valor': sublista[2],
                'data': sublista[3],
                'horario': sublista[4]


            }
            agendamentos.append(agendas)

    return agendas

def listarCompEServ():

    print("\n", "-" * 60)
    print("\nLISTA VENDAS E AGENDAMENTOS:")

    agendamentos = acessarAgendamentos()
    vendas = acessarCompras()

    for agenda in agendamentos:

        print(f"\nUSUARIO: {agenda['nomeUsuario']} | SERVIÇO: {agenda['nomeServico']}"   \
              f"\nVALOR: {agenda['valor']} | DATA: {agenda['data']} | HORARIO: {agenda['horario']}")

    for venda in vendas:

        print(f"\nUSUARIO: {venda['nomeUsuario']} | PRODUTO: {venda['nomeProduto']}"    \
              f"\nQUANTIDADE: {venda['quantidade']} | VALOR: {venda['valorTotal']} ")






