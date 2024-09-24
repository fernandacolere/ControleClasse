import util

arquivo_json = "arquivo_professores.json"

def incluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo = int(input("Por favor, digite o código do professor: "))
    nome = input("Por favor, digite o nome do professor: ")
    cpf = input("Por favor, digite o CPF: ")


    dados = {}
    dados["codigo"] = codigo
    dados["nome"] = nome
    dados["cpf"] = cpf


    # Adicionando porfessor na lista
    lista.append(dados)
    util.salvar_arquivo(lista, arquivo_json)

def listar():
    lista = util.ler_arquivo(arquivo_json)

    if len(lista) <= 0:
        print("Não há professores cadastrados\r\n")

    # Percorrendo a lista mostrando os professores
    for item in lista:
        print(item)

def atualizar():
    lista = util.ler_arquivo(arquivo_json)

    codigo = int(input("Digite o código que deseja editar: "))
    item_atualizar = None

    for item in lista:
        if item["codigo"] == codigo:
            item_atualizar = item
            break

    if item_atualizar == None:
        print(f"Professor de código {codigo} não localizado na lista. ")
    else:
        item_atualizar["codigo"] = int(input("Digite o novo código: "))
        item_atualizar["nome"] = input("Digite o novo nome: ")
        item_atualizar["cpf"] = (input("Digite o novo CPF: "))

        util.salvar_arquivo(lista, arquivo_json)

    for item in lista:
        print(item)

def excluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo = int(input("Digite o código que deseja excluir: "))
    item_removido = None

    for item in lista:
        if item["codigo"] == codigo:
            item_removido = item
            break

    if item_removido == None:
        print(f"Professor de código {codigo} não localizado na lista. ")
    else:
        lista.remove(item)
        print(f"O professor {codigo} foi removido. ")
        util.salvar_arquivo(lista, arquivo_json)