n1, n2 = 1, 1  # Primeiros dois números da sequência de Fibonacci

# Print dos primeiros dois números
print(n1)
print(n2)

# Calcula e mostra os próximos números
for _ in range(58):  # Já temos os dois primeiros, então geramos mais 58
    n3 = n1 + n2
    print(f"{n1} + {n2} = {n3}")  # Exibe a soma
    n1, n2 = n2, n3  # Atualiza n1 e n2 para os próximos cálculos