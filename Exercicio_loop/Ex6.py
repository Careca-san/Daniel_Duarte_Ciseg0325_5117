n = 1
contador = 10

while True:
    n += 1
    # Verificação de número primo
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(f"{n} é um número primo")
        contador -= 1

    if contador == 0:
        break