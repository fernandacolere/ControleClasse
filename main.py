import estudantes
import disciplinas
import professores
import turmas
import matriculas
def mostrar_menu_principal():
    print("Bem-vindo(a) ao menu principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    return input("Digite uma opção válida: ")

def mostrar_menu_secundario():
    print(f"Menu de operações - Opção {opcao}")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")

    return input("Digite uma opção válida: ")

    print("\r\n")  # Quebra de linha para organização

while True:
    opcao = mostrar_menu_principal()

    if opcao == "1":
        print(f"Você escolheu a opção válida {opcao}\r\n")
        while True:
        # Menu secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção {opcao_secundaria}\r\n")

            # Se a opção escolhida for incluir
            if opcao_secundaria == "1":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                estudantes.incluir_estudantes()

            # Se a opção escolhida for listar
            elif opcao_secundaria == "2":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                estudantes.listar_estudantes()

            # Se a opção escolhida for Atualizar
            elif opcao_secundaria == "3":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                estudantes.atualizar_estudantes()

            # Se a opção escolhida for Excluir
            elif opcao_secundaria == "4":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                estudantes.excluir_estudantes()

            elif opcao_secundaria == "5":
                break
            else:
                print("Você digitou uma opção secundária inválida\r\n")
    elif opcao == "2":
        print(f"Você escolheu a opção válida {opcao}\r\n")
        while True:
            # Menu secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção {opcao_secundaria}\r\n")

            # Se a opção escolhida for incluir
            if opcao_secundaria == "1":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                disciplinas.incluir()

            # Se a opção escolhida for listar
            elif opcao_secundaria == "2":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                disciplinas.listar()

            # Se a opção escolhida for Atualizar
            elif opcao_secundaria == "3":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                disciplinas.atualizar()

            # Se a opção escolhida for Excluir
            elif opcao_secundaria == "4":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                disciplinas.excluir()

            elif opcao_secundaria == "5":
                break
            else:
                print("Você digitou uma opção secundária inválida\r\n")
    elif opcao == "3":
        print(f"Você escolheu a opção válida {opcao}\r\n")
        while True:
            # Menu secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção {opcao_secundaria}\r\n")

            # Se a opção escolhida for incluir
            if opcao_secundaria == "1":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                professores.incluir()

            # Se a opção escolhida for listar
            elif opcao_secundaria == "2":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                professores.listar()

            # Se a opção escolhida for Atualizar
            elif opcao_secundaria == "3":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                professores.atualizar()

            # Se a opção escolhida for Excluir
            elif opcao_secundaria == "4":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                professores.excluir()

            elif opcao_secundaria == "5":
                break
            else:
                print("Você digitou uma opção secundária inválida\r\n")
    elif opcao == "4":
        print(f"Você escolheu a opção válida {opcao}\r\n")
        while True:
            # Menu secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção {opcao_secundaria}\r\n")

            # Se a opção escolhida for incluir
            if opcao_secundaria == "1":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                turmas.incluir()

            # Se a opção escolhida for listar
            elif opcao_secundaria == "2":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                turmas.listar()

            # Se a opção escolhida for Atualizar
            elif opcao_secundaria == "3":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                turmas.atualizar()

            # Se a opção escolhida for Excluir
            elif opcao_secundaria == "4":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                turmas.excluir()

            elif opcao_secundaria == "5":
                break
            else:
                print("Você digitou uma opção secundária inválida\r\n")
    elif opcao == "5":
        print(f"Você escolheu a opção válida {opcao}\r\n")
        while True:
            # Menu secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção {opcao_secundaria}\r\n")

            # Se a opção escolhida for incluir
            if opcao_secundaria == "1":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                matriculas.incluir()

            # Se a opção escolhida for listar
            elif opcao_secundaria == "2":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                matriculas.listar()

            # Se a opção escolhida for Atualizar
            elif opcao_secundaria == "3":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                matriculas.atualizar()

            # Se a opção escolhida for Excluir
            elif opcao_secundaria == "4":
                print(f"Você escolheu a opção secundária válida {opcao_secundaria}\r\n")

                matriculas.excluir()

            elif opcao_secundaria == "5":
                break
            else:
                print("Você digitou uma opção secundária inválida\r\n")
    elif opcao == "0":
        print("Saindo . . . ")
        break
    else:
        print("Você digitou uma opção inválida\r\n")