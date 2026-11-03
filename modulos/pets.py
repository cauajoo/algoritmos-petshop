from modulos import validacao
from modulos import memoria

def cadastroPet():

    nome = input("\nDIGITE O NOME DO PET: ")

    while not validacao.verificaVazio(nome):

        nome = input("\nDIGITE O NOME DO PET: ")
    
    tipo = input("\nDIGITE O TIPO DO PET (CACHORRO/GATO/OUTRO): ")

    while not validacao.verificaVazio(tipo):

        tipo = input("\nDIGITE O TIPO DO PET (CACHORRO/GATO/OUTRO): ")

    idadePet = input("\nDIGITE A IDADE DO PET: ")

    while not validacao.verificaVazio(idadePet) or not validacao.verificaIdade(idadePet):

        idadePet = input("\nDIGITE A IDADE DO PET: ")

    raca = input("\nDIGITE A RAÇA DO PET: ")

    while not validacao.verificaVazio(raca):

        raca = input("\nDIGITE A RAÇA DO PET: ")

    idPet = '-' + str(len(nome)) + str(len(tipo)) + idadePet + str(len(raca)) + '-'

    idPet = validacao.verificaIdPetRepetido(idPet)

    print("\nID GERADO PARA O PET:", idPet)

    memoria.salvarPet(idPet, nome, tipo, idadePet, raca)

    print("\nCADASTRO DE PET REALIZADO COM SUCESSO!")

    return idPet

def listarPet(usuario):
    
    pets = memoria.acessarPet()

    print("\n", "-" * 60)
    print("\nLISTA DE PETS:")

    for pet in pets:

        if pet["idPet"] in usuario['idPet']:

            print(f"\nNOME: {pet['nome']} | IDENTIDADE: {pet['idPet']}"  \
                    f"\nTIPO: {pet['tipo']} | IDADE: {pet['idade']}" \
                    f"\nRAÇA: {pet['raca']}")


