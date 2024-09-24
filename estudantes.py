import util

arquivo_json = "arquivo_estudante.json"

def incluir_estudantes():
    lista_estudantes = util.ler_arquivo(arquivo_json)

    codigo = int(input("Por favor, digite o código de estudante: "))
    nome = input("Por favor, digite o nome do estudante: ")
    cpf = input("Por favor, digite o CPF: ")

    dados_estudante = {}
    dados_estudante["codigo"] = codigo
    dados_estudante["nome"] = nome
    dados_estudante["cpf"] = cpf

    # Adicionando o estudante na lista
    lista_estudantes.append(dados_estudante)
    util.salvar_arquivo(lista_estudantes, arquivo_json)

def listar_estudantes():
    estudantes = util.ler_arquivo(arquivo_json)
    if len(estudantes) <= 0:
        print("Não há estudantes cadastrados\r\n")

    # Percorrendo a lista e mostrando os estudantes
    for estudante in estudantes:
        print(estudante)

def atualizar_estudantes():
    estudantes = util.ler_arquivo(arquivo_json)

    codigo_para_editar = int(input("Digite o código que deseja editar: "))
    est_atualizar = None
    for dicionario_estudante in estudantes:
        if dicionario_estudante["codigo"] == codigo_para_editar:
            est_atualizar = dicionario_estudante
            break

    if est_atualizar == None:
        print(f"Estudante de código {codigo_para_editar} não localizado na lista. ")
    else:
        est_atualizar["codigo"] = int(input("Digite o novo código: "))
        est_atualizar["nome"] = input("Digite o novo nome: ")
        est_atualizar["cpf"] = (input("Digite o novo CPF: "))
        util.salvar_arquivo(estudantes, arquivo_json)

    for estudante in estudantes:
        print(estudante)

def excluir_estudantes():
    estudantes = util.ler_arquivo(arquivo_json)

    codigo_para_excluir = int(input("Digite o código que deseja excluir: "))
    est_removido = None
    for dicionario_estudante in estudantes:
        if dicionario_estudante["codigo"] == codigo_para_excluir:
            est_removido = dicionario_estudante
            break

    if est_removido == None:
        print(f"Estudante de código {codigo_para_excluir} não localizado na lista. ")
    else:
        estudantes.remove(dicionario_estudante)
        print(f"O estudante {codigo_para_excluir} foi removido. ")
        util.salvar_arquivo(estudantes, arquivo_json)