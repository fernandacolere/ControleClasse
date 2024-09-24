import json

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            estudantes = json.load(arquivo_aberto)

        return estudantes
    except:
        return []
