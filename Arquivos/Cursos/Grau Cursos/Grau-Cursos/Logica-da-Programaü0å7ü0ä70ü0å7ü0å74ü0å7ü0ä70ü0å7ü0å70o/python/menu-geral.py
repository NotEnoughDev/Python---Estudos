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
        print("4. Atividades do Portugol")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            notes_menu()
        elif opcao == '2':
            print("2")
        elif opcao == '3':
            python_exercises_menu()
        elif opcao == '4':
            print("4")
        elif opcao == '5':
            print("Saindo.......")
            print("\nPrograma Finalizado")
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
        print("3. Voltar para o Menu Principal") 
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("---------------------------------------")
            print("Olá Mundo")
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

def python_exercises_menu():
    while True:
        print("\n=== Menu de Atividades do Python ===")
        print("\n--- Opções ---")
        print("1. Dobro de um Numero")
        print("2. Par ou Impar")
        print("3. Numero Secreto")
        print("4. Soma Acumulativa")
        print("5. Tabuada")
        print("6. Cardapio")
        print("7. Voto")
        print("8. Voltar para o Menu principal")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Dobro de um Numero")
            print("---------------------------------------")
            numero= int(input("\nDigite um número: "))
            dobro = numero*2
            print (f"O dobro de {numero} é {dobro}")
            print("\n---------------------------------------")
        elif opcao == '2':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Par ou Impar")
            print("---------------------------------------")
            numero= int(input("Digite um número: "))
            if numero %2==0:
                print (f"O número {numero} é par")
                print("\n---------------------------------------")
            else:
                print (f"O número {numero} é impar")
                print("\n---------------------------------------")
        elif opcao == '3':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Numero Secreto")
            print("---------------------------------------")    
            import random
            numero_secreto = random.randint(1,10)
            tentativas =0
            contagem_tentativas =0
            numero=0
            print("Bem vindo ao jogo do Número secreto")
            print("Tente advinhar o número secreto 1 e 10")

            while tentativas != numero_secreto:
                numero = float(input("\nDigite um numero: "))
                contagem_tentativas= contagem_tentativas+1
                if numero == numero_secreto:
                    print("\nVocê Adivinhou o número!")
                    print(f"Você precisou de {contagem_tentativas} tentativas")
                    print("\n---------------------------------------")
                    break
                elif numero < numero_secreto:
                    print ("O número secreto é maior.")
                else:
                    print("O número secreto é menor.")
        elif opcao == '4':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Soma Acumulativo")
            print("---------------------------------------") 
            soma= 0
            numero =1
            while numero !=0:
                numero = int(input("Digite um número (0 para sair): "))
                soma = soma + numero
                if numero!=0:
                    print(f"\nA soma até o momento: {soma} ")
                    print(f"A soma dos números digitados é: {soma}")
                    print("\n---------------------------------------")
        elif opcao == '5':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Tabuada")
            print("---------------------------------------") 
            numero= int(input("Digite um número: "))
            for i in range (11):
                print(f"{numero} x {i} = {numero*i}")
                print("\n---------------------------------------")
        elif opcao == '6':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Cardapio")
            print("---------------------------------------") 
            opcao = 0
            while opcao != 5:
                print("\n=== Cardápio ===")
                print("\n1- Hamburguer")
                print("2- Pizza")
                print("3- Salada")
                print("4- Refrigerante")
                print("5- Sair")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    print("\nVocê escolheu hamburguer!")
                    print("---------------------------------------")
                elif opcao == 2:
                    print("\nVocê escolheu pizza!")
                    print("---------------------------------------")
                elif opcao == 3:
                    print("\nVocê escolheu salada!")
                    print("---------------------------------------")
                elif opcao == 4:
                    print("\nVocê escolheu refrigerante!")
                    print("---------------------------------------")
                elif opcao == 5:
                    print("\nSaindo do cardapio..........")
                    print("---------------------------------------")
                    break
                else:
                    print("Opção inválida. Tente novamente!")
                    print("\n---------------------------------------")
        elif opcao == '7':
            print("\nOlá Mundo!")
            print("---------------------------------------")
            print("Voto")
            print("---------------------------------------") 
            ano_atual=2025
            ano_nascimento= int(input("Digite seu ano de nascimento: "))
            idade = ano_atual- ano_nascimento
            print(f"Você tem {idade} anos.")
            if idade <16:
                print("Você não pode votar!")
                print("\n---------------------------------------")
            elif idade <18 or idade >70:
                print("Seu voto é opçional.")
                print("\n---------------------------------------")
            elif idade >=18:
                print("Seu voto é obrigatorio.")
                print("\n---------------------------------------")

        elif opcao == '8':
            break
        else:
            print ("Opção Invalida")

main_menu()
        

        
         

