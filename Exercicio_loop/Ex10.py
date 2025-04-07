# Pedido dum número
numero = int(input("Introduz um número: "))

# Variável para contar divisores
divisores = 0

# Loop de 1 até ao número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

# Print do resultado
print(f"O número {numero} tem {divisores} divisores.")