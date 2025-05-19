def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Opções de Configuração")
        print("2. Opções de Relatórios")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            submenu_configuracao()
        elif escolha == '2':
            submenu_relatorios()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def submenu_configuracao():
    while True:
        print("\n--- Submenu de Configuração ---")
        print("1. Alterar idioma")
        print("2. Ajustar data/hora")
        print("3. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("Idioma alterado com sucesso.")
        elif escolha == '2':
            print("Data/hora ajustadas.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def submenu_relatorios():
    while True:
        print("\n--- Submenu de Relatórios ---")
        print("1. Relatório diário")
        print("2. Relatório mensal")
        print("3. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("Relatório diário gerado.")
        elif escolha == '2':
            print("Relatório mensal gerado.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu_principal()
