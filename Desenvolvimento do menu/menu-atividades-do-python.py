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
            print("Programa Finalizado!")
            break
        else:
            print ("Opção Invalida")

python_exercises_menu()