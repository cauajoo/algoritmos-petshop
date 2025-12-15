from modulos import memoria
from modulos import validacao
from modulos import menus

def cadastrarServicos():

    print("\n", "-" * 60)
    print("CADASTRO DE SERVIÇOS: ")

    nomeServicos = input("\nDIGITE O NOME DO SERVIÇO: ")

    while not validacao.verificaVazio(nomeServicos) or not validacao.verificaServicoRepetido(nomeServicos):

        nomeServicos = input("\nDIGITE O NOME DO SERVIÇO: ")

    valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))

    while not validacao.verificaValor(valorServicos):

        valorServicos = float(input("\nDIGITE O VALOR DO SERVIÇO: "))

    servicosDatas = {}
    
    while True:

        print("\nEXEMPLO: 12/11/2025")
        datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ")

        while not validacao.verificaDatas(datas):

            print("\nEXEMPLO: 12/11/2025")
            datas = input("DIGITE UMA DATA DISPONÍVEL COMO NO EXEMPLO: ")

        print("\nEXEMPLO: 08:00/10:00/12:00")
        horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NESTA DATA: ")

        while not validacao.verificaVazio(horas) or not validacao.verificaHoras(horas):

            print("\nEXEMPLO: 08:00/10:00/12:00")
            horas = input("DIGITE OS HORÁRIOS DISPONÍVEIS NOVAMENTE: ")

        horasLista = horas.split("/")

        servicosDatas[datas] = horasLista

        opcao_2 = input("\nDESEJA FAZER O CADASTRO DE OUTRA DATA (S/N)? ").lower()

        while not validacao.verificaBoolean(opcao_2):

            opcao_2 = input("\nDIGITE NOVAMENTE: ").lower()

        if (opcao_2 == 'n'):

            print("\nCADASTRO DA(S) DATA(S) REALIZADO!")
            break

    memoria.salvarServicos(nomeServicos, valorServicos, servicosDatas)

def listarServicos():

    servicos = memoria.acessarServicos()

    print("\n", "-" * 60)
    print("\nLISTA DE SERVIÇOS:")

    for servico in servicos:

        print(f"\nNOME: {servico['nome']} | VALOR: R${servico['valor']}")

        for data in servico['datas']:

            horarios = servico['datas'][data]

            print(f"\nDATA: {data}")
            print("HORÁRIOS:")

            for i in range(len(horarios)):

                print("-", horarios[i])

    return None

def removerServicos():

    print("\n", "-" * 60)
    print("ATUALIZAR SERVIÇOS")

    listarServicos()

    nomeServicoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    while not validacao.verificaVazio(nomeServicoAcao):

        nomeServicoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    opcao = input(f"\nDESEJA REALMENTE REMOVER O PRODUTO {nomeServicoAcao} (S/N)? ")

    while not validacao.verificaVazio(opcao) and not validacao.verificaBoolean(opcao):
 
        opcao = input(f"\nDESEJA REALMENTE REMOVER O PRODUTO {nomeServicoAcao} (S/N)? ")

    if opcao == "s":

        memoria.removerProduto(nomeServicoAcao)

def agendarServicos(usuario):

    listarServicos()

    nomeServicoAcao = input("\nDIGITE O NOME DO SERVIÇO: ")

    while not validacao.verificaVazio(nomeServicoAcao):
        nomeServicoAcao = input("\nDIGITE O NOME DO SERVIÇO: ")

    servicos = memoria.acessarServicos()
    servicoEncontrado = None

    for servico in servicos:
        if servico['nome'] == nomeServicoAcao:
            servicoEncontrado = servico
            break

    if servicoEncontrado is None:
        print("\nSERVIÇO NÃO ENCONTRADO!")
        return

    data = input("\nDIGITE A DATA (EX: 13/01/2026): ").strip()

    while not validacao.verificaDatas(data):
        data = input("\nDIGITE A DATA (EX: 13/01/2026): ").strip()

    if data not in servicoEncontrado['datas']:
        print("\nDATA NÃO DISPONÍVEL!")
        return

    print("\nHORÁRIOS DISPONÍVEIS:")
    for h in servicoEncontrado['datas'][data]:
        print("-", h)

    horario = input("\nDIGITE O HORÁRIO DESEJADO: ")

    horarios_limpos = [h.strip() for h in servicoEncontrado['datas'][data]]

    if horario not in horarios_limpos:

        print("\nHORÁRIO INVÁLIDO!")

        return agendarServicos(usuario)
    
    opcao = input(f"\nDESEJA REALMENTE AGENDAR O SERVIÇO {servicoEncontrado['nome']} NO VALOR DE R${servicoEncontrado['valor']} (S/N)? ")

    while not validacao.verificaBoolean(opcao):

        opcao = input(f"\nDESEJA REALMENTE AGENDAR O SERVIÇO {servicoEncontrado['nome']} NO VALOR DE R${servicoEncontrado['valor']} (S/N)? ")

    if opcao.lower() == 's':

        for h in servicoEncontrado['datas'][data]:

            if h.strip() == horario:

                servicoEncontrado['datas'][data].remove(h)

                break

        if len(servicoEncontrado['datas'][data]) == 0:
            del servicoEncontrado['datas'][data]

        for servico in servicos:

            memoria.atualizarServico(servicoEncontrado['nome'], servico['nome'], servico['valor'], servico['datas'])

        memoria.salvarAgendamentos(usuario['nome'], servicoEncontrado['nome'], servicoEncontrado['valor'], data, horario)

        print("\nAGENDAMENTO REALIZADO COM SUCESSO!")
    
    else:

        print("\nVOLTANDO PARA O MENU ANTERIOR...")

    