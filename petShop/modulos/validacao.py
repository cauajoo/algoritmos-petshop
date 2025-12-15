from datetime import datetime

rota = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\usuarios.txt"
rota1 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\pets.txt"
rota2 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\produtos.txt"
rota3 = "C:\\Users\\Cauã João\\Desktop\\FACULDADE\\2025.2\\ALGORITIMO\\petShop\\memoria\\servicos.txt"


def verificaEmail(email):

    email = email.strip()

    if (len(email) < 12):

        print("\nEMAIL INVÁLIDO! MUITO CURTO, NO MÍNIMO 12 CARACTERES.")

        return False
    
    if ('@' not in email):

        print("\nEMAIL INVÁLIDO! FALTA O '@'")

        return False
    
    if ('.com' not in email):

        print("\nEMAIL INVÁLIDO! FALTA O '.com'")

        return False
    
    if ('gmail' not in email and 'hotmail' not in email and 'outlook' not in email):

        print("\nEMAIL INVÁLIDO! FALTA O DOMINIO 'gmail', 'hotmail' ou 'outlook'")

        return False
    
    return True

def verificaVazio(texto): 

    texto = str(texto).strip()

    if(texto == ""):

        print("OPÇÃO VAZIA! TENTE NOVAMENTE!")

        return False
    
    return True

def verificaCPF(CPF):

    CPF = CPF.strip()

    if (len(CPF) != 11):

        print("\nCPF INVÁLIDO! DEVE CONTER 11 NÚMEROS.")

        return False
    
    if (CPF.isdigit() == False):

        print("\nCPF INVÁLIDO! DEVE CONTER APENAS NÚMEROS.")

        return False
    
    return True

def verificaNumero(numero):

    numero = numero.strip()

    if (len(numero) != 11):

        print("\nNÚMERO INVÁLIDO! DEVE CONTER 11 DIGITOS (DDD + NÚMERO).")

        return False
    
    if (numero.isdigit() == False):

        print("\nNÚMERO INVÁLIDO! DEVE CONTER APENAS MÚMEROS.")

        return False
    
    return True

def verificaIdade(idade):

    idade = idade.strip()

    if (idade.isdigit() == False):

        print("\nIDADE INVÁLIDA! DEVE CONTER APENAS NÚMEROS.")

        return False
    
    if (int(idade) < 0):

        print("\nIDADE INVÁLIDA! NÃO É ACEITO VALORES NEGATIVOS.")

        return False
    
    if (int(idade) > 80):

        print("\nIDADE INVÁLIDA! POR FAVOR INSIRA UMA IDADE VÁLIDA.")

        return False
    
    return True

def verificaSenha(senha):

    senha = senha.strip()

    if (len(senha) < 6):

        print("\nSENHA INVÁLIDA! MUITO CURTA, NO MÍNIMO 6 CARACTERES.")

        return False
    
    if (len(senha) > 12):

        print("\nSENHA INVÁLIDA! MUITO LONGA, NO MÁXIMO 12 CARACTERES.")

        return False
    
    if ('*' not in senha and '#' not in senha and '@' not in senha and '!' not in senha):

        print("\nSENHA INVÁLIDA! DEVE CONTER PELO MENOS UM CARACTER ESPECIAL: '*', '#', '@' OU '!'")

        return False
    
    return True

def verificaBoolean(opcao):

    opcao = opcao.strip().lower()

    if (len(opcao) == 0):

        print("\nOPÇÃO INVÁLIDA! NÃO PODE SER VAZIA.")

        return False

    if (opcao != 'sim' and opcao != 'não' and opcao != 'nao' and opcao != 's' and opcao != 'n'):

        print("\nOPÇÃO INVÁLIDA! DIGITE 'SIM' OU 'NÃO'.")
        
        return False
    
    return True

def verificaValor(valor):

    valor = valor

    if (valor <= 0):

        print("\nVALOR INVÁLIDO! NÃO É ACEITO VALORES NEGATIVOS OU IGUAIS A ZERO.")

        return False
    
    return True

def verificaSenhaColaborador():

    verificacao = input("\nDIGITE A SENHA DE VERIFICAÇÃO DE COLABORADOR: ")

    while not verificaVazio(verificacao):

        verificacao = input("\nDIGITE A SENHA DE VERIFICAÇÃO DE COLABORADOR: ")

    if (verificacao == "Colab@2025"):

        return True
    
    else:

        print("\nSENHA DE VERIFICAÇÃO INVÁLIDA! TENTE NOVAMENTE.")

        return False

def verificaCPFRepetido(CPF):

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (CPF == sublista[1]):

                print("\nCPF JÁ CADASTRADO! TENTE NOVAMENTE.")

                return False
            
    return True

def verificaEmailRepetido(email):

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (email == sublista[2]):

                print("\nEMAIL JÁ CADASTRADO! TENTE NOVAMENTE.")

                return False
            
    return True

def verificaUsuarioLogado():

    with open(rota, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (sublista[8] == 'cliente'):

                if (sublista[7] == 'True'):

                    usuario = {

                        "nome": sublista[0],
                        "CPF": sublista[1],
                        "email": sublista[2],
                        "numero": sublista[3],
                        "idade": sublista[4],
                        "senha": sublista[5],
                        "verificacao": sublista[6],
                        "logado": sublista[7],
                        "tipoUsuario": sublista[8],
                        "idPet": sublista[9].split('-')
                    }
                
                    return usuario
                
            else:

                if (sublista[7] == 'True'):

                    usuario = {

                        "nome": sublista[0],
                        "CPF": sublista[1],
                        "email": sublista[2],
                        "numero": sublista[3],
                        "idade": sublista[4],
                        "senha": sublista[5],
                        "verificacao": sublista[6],
                        "logado": sublista[7],
                        "tipoUsuario": sublista[8]
                    }
                
                    return usuario
            
    return None

def verificaIdPetRepetido(idPet):

    idPet = idPet[1:-1]

    with open(rota1, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if (idPet == sublista[0]):

                idPet = str(int(idPet) + 1)

                return verificaIdPetRepetido(idPet)
            
    return idPet

def verificaProdutoRepetido(nomeProduto):

    with open(rota2, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if nomeProduto == sublista[0]:

                print("PRODUTO JÁ CADASTRADO! TENTE NOVAMENTE!")

                return False
            
        return True
    
def verificaQuantidade(quantidadeProdutos):

    if int(quantidadeProdutos) <= 0:

        print("\nQUANTIDADE INVÁLIDA! NÃO É ACEITO QUANTIDADES NEGATIVAS OU ZERADAS TENTE NOVAMENTE!")
    
        return False
    
    return  True

def verificaDatas(data):

    data = data.strip()

    datas = data.split("/")

    dia = int(datas[0])
    mes = int(datas[1])
    ano = int(datas[2])

    hoje = datetime.today()

    dataData = datetime(ano, mes, dia)

    meses31 = [1, 3, 5, 7, 8, 10, 12]

    mensagem = "\nDATA INVÁLIVA, TENTE NOVAMENTE!"


    if ano < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:

        print(mensagem)

        return False
    
    if ano % 4 == 0 and mes == 2:

        if dia > 29:

            print(mensagem)

            return False
    
    if mes == 2:

        if dia > 28:

            print(mensagem)

            return False
    
    if mes not in meses31:

        if dia > 30:
            
            print(mensagem)

            return False
        
    if dataData < hoje:

        print(mensagem)

        return False
    
    return True

def verificaValidade(dataValidade):

    hoje = datetime.today()

    dataValidade = dataValidade.split("/")

    validade = datetime(int(dataValidade[2]), int(dataValidade[1]), int(dataValidade[0]))

    if hoje > validade:   

        print("\nPRODUTO VENCIDO! ATUALIZE O PRODUTO!")

        return False
    
    return True

def verificaServicoRepetido(nomeServico):

    with open(rota3, "r") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:

            sublista = linha.strip().split(";")

            if nomeServico == sublista[0]:

                print("SERVIÇO JÁ CADASTRADO! TENTE NOVAMENTE!")

                return False
            
        return True

def verificaHoras(horas):

    horas = horas.strip()

    if ':' not in horas:

        print("\n HORÁRIOS INVÁLIDOS! TENTE NOVAMENTE COMO NO EXEMPLO!")
        return False
    
    return True

