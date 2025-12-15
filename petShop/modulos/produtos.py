from modulos import validacao
from modulos import menus
from modulos import memoria

def cadastrarProdutos():

    while True:

        print("\n", "-" * 60)
        print("CADASTRO DE PRODUTO")

        nomeProdutos = input("\nDIGITE O NOME DO PRODUTO: ")
            
        while not validacao.verificaVazio(nomeProdutos) or not validacao.verificaProdutoRepetido(nomeProdutos):

            nomeProdutos = input("\nDIGITE O NOME DO PRODUTO: ")

        tipoProduto = menus.menuTipoProduto()

        valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))

        while not validacao.verificaVazio(valorProdutos) or not validacao.verificaValor(valorProdutos):

            valorProdutos = float(input("\nDIGITE O VALOR DO PRODUTO: "))

        quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO NO ESTOQUE: "))

        while not validacao.verificaVazio(quantidadeProdutos) or not validacao.verificaQuantidade(quantidadeProdutos):

            quantidadeProdutos = int(input("\nDIGITE A QUANTIDADE DO PRODUTO: "))

        print("\nEXEMPLO: 12/12/2012\n")
        validadeProdutos = input("\nDIGITE A DATA DE VALIDADE DO PRDUTO: ")

        while not validacao.verificaVazio(validadeProdutos) or not validacao.verificaDatas(validadeProdutos) and not validacao.verificaValidade(validadeProdutos):

            print("\nEXEMPLO: 12/12/2012\n")
            validadeProdutos = input("\nDIGITE A DATA DE VALIDADE DO PRDUTO: ")

        memoria.salvarProdutos(nomeProdutos, tipoProduto, valorProdutos, quantidadeProdutos, validadeProdutos)

        return None
    
def listarProdutos():

    produtos = memoria.acessarProdutos()

    print("\n", "-" * 60)
    print("\nLISTA DE PRODUTOS:")

    for produto in produtos:

        print(f"\nNOME: {produto['nome']} | VALIDADE: {produto['validade']}"  \
                f"\nVALOR: {produto['valor']} | QUANTIDE: {produto['quantidade']}" \
                f"\nTIPO: {produto['tipo']}")

def atualizarProduto():

    print("\n", "-" * 60)
    print("ATUALIZAR PRODUTOS")

    listarProdutos()

    nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    while not validacao.verificaVazio(nomeProdutoAcao):

        nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    nomeProdutos = input("\nDIGITE O NOVO NOME DO PRODUTO: ")
        
    while not validacao.verificaVazio(nomeProdutos) and not validacao.verificaProdutoRepetido(nomeProdutos):

        nomeProdutos = input("\nDIGITE O NOVO NOME DO PRODUTO: ")

    tipoProduto = menus.menuTipoProduto()

    valorProdutos = float(input("\nDIGITE O NOVO VALOR DO PRODUTO: "))

    while not validacao.verificaVazio(valorProdutos) and not validacao.verificaValor(valorProdutos):

        valorProdutos = float(input("\nDIGITE O NOVO VALOR DO PRODUTO: "))

    quantidadeProdutos = int(input("\nDIGITE A NOVA QUANTIDADE DO PRODUTO NO ESTOQUE: "))

    while not validacao.verificaVazio(quantidadeProdutos) and not validacao.verificaQuantidade(quantidadeProdutos):

        quantidadeProdutos = int(input("\nDIGITE A NOVA QUANTIDADE DO PRODUTO NO ESTOQUE: "))

    print("\nEXEMPLO: 12/12/2012\n")
    validadeProdutos = input("\nDIGITE A NOVA DATA DE VALIDADE DO PRODUTO: ")

    while not validacao.verificaVazio(validadeProdutos) and not validacao.verificaDatas(validadeProdutos) and not validacao.verificaValidade(validadeProdutos):

        print("\nEXEMPLO: 12/12/2012\n")
        validadeProdutos = input("\nDIGITE A NOVA DATA DE VALIDADE DO PRODUTO: ")

    memoria.atualizarProduto(nomeProdutoAcao, nomeProdutos, tipoProduto, valorProdutos, quantidadeProdutos, validadeProdutos)  

    return None

def removerProduto():

    print("\n", "-" * 60)
    print("ATUALIZAR PRODUTOS")

    listarProdutos()

    nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    while not validacao.verificaVazio(nomeProdutoAcao):

        nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO A SER ATUALIZADO: ")

    opcao = input(f"\nDESEJA REALMENTE REMOVER O PRODUTO {nomeProdutoAcao} (S/N)? ")

    while not validacao.verificaVazio(opcao) and not validacao.verificaBoolean(opcao):
 
        opcao = input(f"\nDESEJA REALMENTE REMOVER O PRODUTO {nomeProdutoAcao} (S/N)? ")

    if opcao == "s":

        memoria.removerProduto(nomeProdutoAcao)

def comprarProduto(usuario):

    listarProdutos()

    nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO QUE VOCÊ DESEJA COMPRAR: ")

    while not validacao.verificaVazio(nomeProdutoAcao):

        nomeProdutoAcao = input("\nDIGITE O NOME DO PRODUTO QUE VOCÊ DESEJA COMPRAR: ")

    produtos = memoria.acessarProdutos()

    quantidade = int(input("\nDIGITE A QUANTIDADE: "))

    while not validacao.verificaQuantidade(quantidade):

        quantidade = int(input("\nDIGITE A QUANTIDADE: "))

    for produto in produtos:

        if produto['nome'] == nomeProdutoAcao:

            if int(produto['quantidade']) < int(quantidade):

                print("\nA QUANTIDADE NÃO ESTA DISPONIVEL! TENTE NOVAMENTE.")

            else:

                memoria.realizarCompra(nomeProdutoAcao, quantidade, usuario)







