marcas = []
modelos = []

def menu():
    print("\n-----MENU-----")
    print("1 - Introduzir dados")
    print("2 - Procurar dados")
    print("3 - Eliminar dados")
    print("4 - Sair do programa")

    try:
        opcao = int(input("Escolha uma das opções: "))
        match opcao:
            case 1:
                Introd_dados()
            case 2:
                Proc_dados()
            case 3:
                Apagar_dados()
            case 4:
                print("A sair do programa...")
                exit()
            case _:
                print("Opção inválida.")
                menu()
    except (ValueError, TypeError):
        print("Insira um número válido.")
        menu()

def Introd_dados():
    while len(marcas) < 100:
        marca = input("Por favor, insira a marca do carro: ")
        modelo = input("Por favor, insira o modelo desse carro: ")
        marcas.append(marca)
        modelos.append(modelo)
        continuar = input("Deseja inserir mais carros? (s/n): ").lower()
        if continuar != 's':
            break
    menu()

def Proc_dados():
    procura = input("Que marca ou modelo está à procura? ").lower()
    encontrado = False
    for i in range(len(marcas)):
        if procura in marcas[i].lower() or procura in modelos[i].lower():
            print(f"Posição {i}: Marca - {marcas[i]}, Modelo - {modelos[i]}")
            encontrado = True
    if not encontrado:
        print("Nenhum resultado encontrado.")
    menu()

def Apagar_dados():
    if not marcas:
        print("A lista está vazia.")
        menu()
        return

    try:
        for i in range(len(marcas)):
            print(f"{i} - {marcas[i]} {modelos[i]}")
        pos = int(input("Insira a posição do carro que deseja apagar: "))
        if 0 <= pos < len(marcas):
            print(f"Vai apagar: {marcas[pos]} {modelos[pos]}")
            confirmar = input("Tem a certeza? (s/n): ").lower()
            if confirmar == 's':
                marcas.pop(pos)
                modelos.pop(pos)
                print("Carro apagado com sucesso.")
            else:
                print("Cancelado.")
        else:
            print("Posição inválida.")
    except (ValueError, TypeError):
        print("Insira um número válido.")
    menu()

menu()