# Pede um número
limite = int(input("Introduz um número: "))

contador = 0  # Contador de números perfeitos encontrados

print(f"\nNúmeros perfeitos entre 1 e {limite}:")

# Percorre os números de 1 até ao limite
for num in range(1, limite + 1):
    soma_divisores = 0

    # Soma todos os divisores próprios (excluindo o próprio número)
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i

    # Verifica se é número perfeito
    if soma_divisores == num:
        print(num)
        contador += 1

# Print do total
print(f"\nTotal de números perfeitos encontrados: {contador}")