soma = 0
contador = 0

print("Introduza 30 números pares entre 1 e 50:")

while contador < 30:
    try:
        num = int(input(f"Número {contador + 1}: "))

        # Verifica se está no intervalo permitido
        if num < 1 or num > 50:
            print("O número deve estar entre 1 e 50.")
            continue

        # Verifica se é par
        if num % 2 != 0:
            print("O número deve ser par.")
            continue

        # Caso o número seja válido
        soma += num
        contador += 1

    except ValueError:
        print("Entrada inválida! Introduza um número inteiro.")

# Calcula a média
media = soma / 30
print(f"\nA média dos 30 números pares introduzidos é: {media}")