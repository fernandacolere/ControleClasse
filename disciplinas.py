import util

disciplinas_json = "arquivo_disciplina.json"

def incluir():
    lista = util.ler_arquivo(disciplinas_json)

    codigo = int(input("Por favor, digite o código da disciplina: "))
    nome = input("Por favor, digite o nome da disciplina: ")

    dados = {}
    dados["codigo"] = codigo
    dados["nome"] = nome

    # Adicionando a discplina na lista
    lista.append(dados)
    util.salvar_arquivo(lista, disciplinas_json)

def listar():
    lista = util.ler_arquivo(disciplinas_json)

    if len(lista) <= 0:
        print("Não há disciplinas cadastradas\r\n")

    # Percorrendo a lista mostrando as disciplinas
    for item in lista:
        print(item)

def atualizar():
    lista = util.ler_arquivo(disciplinas_json)

    codigo = int(input("Digite o código que deseja editar: "))
    item_atualizar = None

    for item in lista:
        if item["codigo"] == codigo:
            item_atualizar = item
            break

    if item_atualizar == None:
        print(f"Disciplina de código {codigo} não localizada na lista. ")
    else:
        item_atualizar["codigo"] = int(input("Digite o novo código: "))
        item_atualizar["nome"] = input("Digite o novo nome: ")
        util.salvar_arquivo(lista, disciplinas_json)

    for item in lista:
        print(item)

def excluir():
    lista = util.ler_arquivo(disciplinas_json)

    codigo = int(input("Digite o código que deseja excluir: "))
    item_removido = None

    for item in lista:
        if item["codigo"] == codigo:
            item_removido = item
            break

    if item_removido == None:
        print(f"Disciplina de código {codigo} não localizada na lista. ")
    else:
        lista.remove(item)
        print(f"A disciplina {codigo} foi removida. ")
        util.salvar_arquivo(lista, disciplinas_json)