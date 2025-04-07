numeros = []

#Adicionar 10 números à escolha
for i in range(0,10):
    num = int(input("Insira um número: "))
    numeros.append(num)

#Print dos números pares
for num in numeros:
    if num % 2 == 0:
        print(f"Número par: {num}")

#Print dos números impares
for num in numeros:
    if num % 2 != 0:
        print(f"Número impar: {num}")
        