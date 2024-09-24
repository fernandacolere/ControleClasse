import util

arquivo_json = "arquivo_matriculas.json"

def incluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo_turma = int(input("Por favor, digite o código da turma: "))
    codigo_estudante = int(input("Por favor, digite o código do estudante: "))
    for item in lista:
        if item["codigo_turma"] == codigo_turma and item["codigo_estudante"] == codigo_estudante:
            print("Matrícula já cadastrada para está turma e estudante")
            return
    dados = {}
    dados["codigo_turma"] = codigo_turma
    dados["codigo_estudante"] = codigo_estudante

    # Adicionando codigos na lista
    lista.append(dados)
    util.salvar_arquivo(lista, arquivo_json)

def listar():
    lista = util.ler_arquivo(arquivo_json)

    if len(lista) <= 0:
        print("Não há matriculas cadastradas\r\n")

    # Percorrendo a lista mostrando as matriculas
    for item in lista:
        print(item)

def atualizar():
    lista = util.ler_arquivo(arquivo_json)

    codigo_turma = int(input("Digite o código da turma que deseja editar a matrícula: "))
    codigo_estudante = int(input("Digite o código do estudante que deseja editar a matrícula: "))

    item_atualizar = None

    for item in lista:
        if item["codigo_turma"] == codigo_turma and item["codigo_estudante"] == codigo_estudante:
            item_atualizar = item
            break

    if item_atualizar == None:
        print(f" Não foi possível localizar a matrícula para turma {codigo_turma} e estudante {codigo_estudante}")
    else:
        item_atualizar["codigo_turma"] = int(input("Digite o novo código da turma: "))
        item_atualizar["codigo_estudante"] = int(input("Digite o novo código do estudante: "))

        util.salvar_arquivo(lista, arquivo_json)

    for item in lista:
        print(item)

def excluir():
    lista = util.ler_arquivo(arquivo_json)

    codigo_turma = int(input("Digite o código da turma que deseja excluir a matrícula: "))
    codigo_estudante = int(input("Digite o código do estudante que deseja excluir a matrícula: "))
    item_removido = None

    for item in lista:
        if item["codigo_turma"] == codigo_turma and item["codigo_estudante"] == codigo_estudante:
            item_removido = item
            break

    if item_removido == None:
        print(f" Não foi possível localizar a matrícula para turma {codigo_turma} e estudante {codigo_estudante}")
    else:
        lista.remove(item)
        print(f" A matrícula da turma {codigo_turma} e estudante {codigo_estudante} foram removidos")
        util.salvar_arquivo(lista, arquivo_json)