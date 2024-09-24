import util

arquivo_json = "arquivo_turmas.json"

def incluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo_turma = int(input("Por favor, digite o código da turma: "))
    for item in lista:
        if item["codigo_turma"] == codigo_turma:
            print("Turma já cadastrada com este código")
            return
    codigo_professor = int(input("Por favor, digite o código do professor: "))
    codigo_disciplina = int(input("Por favor, digite o código da disciplina: "))


    dados = {}
    dados["codigo_turma"] = codigo_turma
    dados["codigo_professor"] = codigo_professor
    dados["codigo_disciplina"] = codigo_disciplina


    # Adicionando codigos na lista
    lista.append(dados)
    util.salvar_arquivo(lista, arquivo_json)

def listar():
    lista = util.ler_arquivo(arquivo_json)

    if len(lista) <= 0:
        print("Não há turmas cadastradas\r\n")

    # Percorrendo a lista mostrando as turmas
    for item in lista:
        print(item)

def atualizar():
    lista = util.ler_arquivo(arquivo_json)

    codigo = int(input("Digite o código da turma que deseja editar: "))
    item_atualizar = None

    for item in lista:
        if item["codigo_turma"] == codigo:
            item_atualizar = item
            break

    if item_atualizar == None:
        print(f"Professor de código {codigo} não localizado na lista. ")
    else:
        item_atualizar["codigo_turma"] = int(input("Digite o novo código: "))
        item_atualizar["codigo_professor"] = int(input("Digite o novo código do professor: "))
        item_atualizar["codigo_disciplina"] = int(input("Digite o novo código da disciplina: "))

        util.salvar_arquivo(lista, arquivo_json)

    for item in lista:
        print(item)

def excluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo = int(input("Digite o código que deseja excluir: "))
    item_removido = None

    for item in lista:
        if item["codigo_turma"] == codigo:
            item_removido = item
            break

    if item_removido == None:
        print(f"Turma de código {codigo} não localizada na lista. ")
    else:
        lista.remove(item)
        print(f"A turma {codigo} foi removida. ")
        util.salvar_arquivo(lista, arquivo_json)