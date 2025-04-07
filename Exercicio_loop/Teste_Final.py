# Função para verificar se um número é primo
def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Função para calcular os divisores de um número
def calcular_divisores(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

# Função para verificar se um número é perfeito
def perfeito(n):
    divisores = calcular_divisores(n)
    soma = sum(divisores) - n  # Exclui o próprio número
    return soma == n

# Função para a calculadora
def calculadora():
    print("\nCalculadora Simples")
    while True:
        try:
            num1 = float(input("Introduza o primeiro número: "))
            operador = input("Escolha a operação (+, -, *, /): ")
            num2 = float(input("Introduza o segundo número: "))
            
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                    continue
                resultado = num1 / num2
            else:
                print("Operação inválida!")
                continue
                
            print(f"Resultado: {resultado}")
            continuar = input("Deseja continuar com outra operação? (s/n): ").lower()
            if continuar != 's':
                break
        except ValueError:
            print("Entrada inválida, por favor insira números válidos.")

# Função para a tabuada
def tabuada():
    print("\nTabuada")
    while True:
        try:
            max_num = int(input("Introduza o número para gerar a tabuada (1-1000): "))
            if max_num < 1 or max_num > 1000:
                print("O número deve ser entre 1 e 1000!")
                continue
            break
        except ValueError:
            print("Entrada inválida, por favor insira um número entre 1 e 1000.")
    
    for i in range(1, max_num + 1):
        print(f"\nTabuada do {i}:")
        for j in range(1, max_num + 1):
            print(f"{i} x {j} = {i * j}")
        print("-" * 20)

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Ver números primos, divisores e números perfeitos até um número")
        print("2. Calculadora Simples (+, -, *, /) e Tabuada")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2, 3): ")
        
        if opcao == "1":
            # Parte de números primos, divisores e números perfeitos
            while True:
                try:
                    limite = int(input("Introduza um número entre 1 e 30000: "))
                    if limite < 1 or limite > 30000:
                        print("O número deve ser entre 1 e 30.000!")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida, por favor insira um número entre 1 e 30000.")
            
            for num in range(limite, 0, -1):
                print(f"\nNúmero: {num}")
                # Verificar se o número é primo
                if primo(num):
                    print(f"{num} é um número primo.")
                else:
                    print(f"{num} não é um número primo.")
                
                # Calcular divisores
                divisores = calcular_divisores(num)
                print(f"Divisores de {num}: {divisores}")
                
                # Verificar se é perfeito
                if perfeito(num):
                    print(f"{num} é um número perfeito.")
                else:
                    print(f"{num} não é um número perfeito.")
                
                # Pausar a cada 10 números
                if num % 10 == 0:
                    continuar = input("Deseja continuar? (s/n): ").lower()
                    if continuar != "s":
                        break

        elif opcao == "2":
            # Calculadora simples e tabuada
            while True:
                print("\nEscolha uma opção:")
                print("1. Calculadora Simples")
                print("2. Tabuada")
                print("3. Voltar ao menu principal")
                escolha = input("Escolha uma opção (1, 2, 3): ")

                if escolha == "1":
                    calculadora()
                elif escolha == "2":
                    tabuada()
                elif escolha == "3":
                    break
                else:
                    print("Opção inválida, tente novamente.")

        elif opcao == "3":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()