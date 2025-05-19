print ("Olá Mundo\n")
print ("Seja Bem vindo ao meu 'Menu de Atividades'")
print ("Aqui colocarei as anotações das atividades feitas durante meu curso mais anotações\n")

def main_menu():
    while True:
        print("\n=== Menu Principal ===")
        print("\n--- Opções ---")
        print("1. Anotações sobre o Python")
        print("2. Anotações sobre o Portugol")
        print("3. Atividades do Python")
        print("4. Atividades do Python")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            notes_menu()
        elif opcao == '2':
            print("2")
        elif opcao == '3':
            print("3")
        elif opcao == '4':
            print("4")
        elif opcao == '5':
            print("5")
            break
        else:
            print ("Opção Invalida")
            main_menu()

def notes_menu():
    while True:
        print("\n=== Menu de Anotações do Python ===")
        print("\n--- Opções ---")
        print("1. Notas do Python")
        print("2. Desenvolvimento do Menu Geral")
        print("3. Voltar") 
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("---------------------------------------")
            print("\nOlá Mundo")
            print("---------------------------------------")
            print("Anotações sobre o Python")
            print("---------------------------------------")
            print("input = É um comando como o "'Leia (Variavel)'" do portugol onde se escreve na mesma linha que a usa.")
            print("Em outras palavras, um comando para poder dar entrada de dados ou informações ao programa.")
            print("   Exemplo: 'nome= input (Digite seu nome: )'")
            print("   Nesse exemplo, se colocasse isso num programa Python, poderei escrever algo")
            print("\nfloat = Variavel de n° reais")
            print("\nint = Variavel de nº inteiros")
            print("\n'f' = Comando usado para referir uma variavel de maneira mais rapida. Geralmente, quando for referida, usar '{'}'")
            print("\nif = Se")
            print("\nif not = Se não(Caso contrario)")
            print("\nelse = Senão")
            print("\nelif = Senão se")
            print("\nprint = Escreva")
            print("'==' = Igual comparativo")
            print("':' = Substituição das chaves do Portugol ou seja, blocos de comando.")
            print("---------------------------------------")
        if opcao == '2':
            print("---------------------------------------")
            print("Por que perder tempo fazendo esse menu?")
            print("\nNa epoca, eu quis me desafiar programando além do que sabia, me forçando a buscar a aprender mais. Esse menu, por exemplo nasceu assim.")
            print("\n\nComo exatamente essa ideia de menu nasceu?")
            print("\nQuando estava aprendendo logica da programação com o Portugol tinha decidido aprender programação com esse mesmo objetivo, se tinha como fazer um menu para mim seria um programa e assim, depois de ser introduzido ao Python, fiz o mesmo.")
            print("\n\nTirei alguma referência? Busquei algum conhecimento?")
            print("\nSim, eu tirei uma referência, no caso, da propria ia da google e sim, busquei me apronfundar para fazer esse menu se tornar realidade. Alias uma curiosidade é de que escrevi isso em 12 de Maio de 2025 as 19:32pm e que nesse tempo, o menu ainda não estava pronto então.... saudações do passado ;)")
            print("---------------------------------------")
        if opcao == '3':
            break
main_menu()
        

        
         

