print("Múltiplos de 5 que não são múltiplos de 3 (de 1 a 1000):\n")

# Print dos números
for num in range(1, 1001):
    if num % 5 == 0 and num % 3 != 0:
        print(num)