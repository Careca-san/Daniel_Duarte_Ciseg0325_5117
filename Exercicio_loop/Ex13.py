# Pedido dum número para fazer a tabuada
numero = int(input("Introduz um número para ver a tabuada: "))

# Mostra a tabuada do número pedido de 1 a 10
print(f"\nTabuada do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")