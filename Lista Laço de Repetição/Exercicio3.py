while True:
print("MENU de Linguagens de Programação:")
print("1. Python")
print("2. Java")
print("3. JavaScript")
print("4. C++")
print("5. Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Você escolheu a melhor linguagem de programação: Python!!!")
elif opcao == "2":
    print("Você escolheu a segunda opção: Java")
elif opcao == "3":
    print("Você escolheu a terceira opção: JavaScript")
elif opcao == "4":
    print("Você escolheu a quarta opção: C++")
elif opcao == "5":
    print("Você está saindo do sistema...")
    break
else:
    print("Opção inválida. Tente novamente!")