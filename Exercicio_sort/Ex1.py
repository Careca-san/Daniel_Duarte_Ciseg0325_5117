# Função para adicionar uma pessoa à lista
def adicionar(lista, primeiro, ultimo, idade):
    lista.append((primeiro, ultimo, idade))

# Função para remover pessoas com base no primeiro ou último nome
def remover(lista, nome, por_primeiro=True):
    removidos = 0
    nova_lista = []
    for pessoa in lista:
        alvo = pessoa[0] if por_primeiro else pessoa[1]
        igual = True
        if len(alvo) != len(nome):
            igual = False
        else:
            for i in range(len(nome)):
                if ord(alvo[i]) != ord(nome[i]):
                    igual = False
                    break
        if not igual:
            nova_lista.append(pessoa)
        else:
            removidos += 1
    # Substitui o conteúdo da lista original
    lista[:] = nova_lista
    return removidos

# Validação do nome com base na tabela ASCII
def nome_valido(nome):
    if len(nome) == 0:
        return False
    primeira = ord(nome[0])
    if not (65 <= primeira <= 90 or 192 <= primeira <= 222):  # A-Z e letras maiúsculas acentuadas
        return False
    for letra in nome[1:]:
        codigo = ord(letra)
        if not ((97 <= codigo <= 122) or (224 <= codigo <= 255)):  # a-z e letras minúsculas acentuadas
            return False
    return True

# Lista de pessoas
pessoas = []

# Ciclo principal
while True:
    print("\n--- MENU ---\n1. Adicionar pessoa\n2. Listar por primeiro nome\n3. Listar por último nome\n4. Remover por primeiro nome\n5. Remover por último nome\n6. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        primeiro = input("Primeiro nome: ")
        ultimo = input("Último nome: ")
        
        if nome_valido(primeiro) and nome_valido(ultimo):
            idade_str = input("Idade: ")
            idade_valida = True
            for caractere in idade_str:
                if ord(caractere) < 48 or ord(caractere) > 57:  # verifica se é dígito (0–9)
                    idade_valida = False
                    break
            if idade_valida:
                idade = 0
                for caractere in idade_str:
                    idade = idade * 10 + (ord(caractere) - 48)
                adicionar(pessoas, primeiro, ultimo, idade)
                print("Pessoa adicionada com sucesso.")
            else:
                print("Erro: Idade inválida.")
        else:
            print("Erro: Nome mal formatado.")

    elif opcao == "2":
        pessoas.sort(key=lambda p: [ord(caractere) for caractere in p[0]])
        print("\n--- Lista por Primeiro Nome ---")
        for p in pessoas:
            print(p[0] + " " + p[1] + " - " + str(p[2]) + " anos")

    elif opcao == "3":
        pessoas.sort(key=lambda p: [ord(caractere) for caractere in p[1]])
        print("\n--- Lista por Último Nome ---")
        for p in pessoas:
            print(p[0] + " " + p[1] + " - " + str(p[2]) + " anos")

    elif opcao == "4":
        nome = input("Primeiro nome a remover: ")
        removidos = remover(pessoas, nome, por_primeiro=True)
        if removidos:
            print("Removida(s) " + str(removidos) + " pessoa(s).")
        else:
            print("Nome não encontrado.")

    elif opcao == "5":
        nome = input("Último nome a remover: ")
        removidos = remover(pessoas, nome, por_primeiro=False)
        if removidos:
            print("Removida(s) " + str(removidos) + " pessoa(s).")
        else:
            print("Nome não encontrado.")

    elif opcao == "6":
        print("A sair...")
        break

    else:
        print("Opção inválida.")