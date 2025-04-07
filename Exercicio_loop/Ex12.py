# Pedido dum número
limite = int(input("Introduz um número: "))

# Variável para contar operações
operacoes = 0

# Percorre todos os números menores que o introduzido
for i in range(1, limite):
    soma = limite + i
    subtracao = limite - i
    multiplicacao = limite * i
    divisao = limite / i  # i nunca será zero, começa em 1

    # Print dos resultados das operações
    print(f"{limite} + {i} = {soma}")
    print(f"{limite} - {i} = {subtracao}")
    print(f"{limite} * {i} = {multiplicacao}")
    print(f"{limite} / {i} = {divisao}")
    print("-" * 20)

    # Incrementa o contador
    operacoes += 4

# Print do total de operações efetuadas
print(f"\nTotal de operações efetuadas: {operacoes}")