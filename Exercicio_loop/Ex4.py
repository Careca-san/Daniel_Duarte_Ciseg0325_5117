#Pedir um número inteiro
n = int(input("Insira um número inteiro: "))

#Verificar se é primo
if n < 2:
    print(f"{n} não é um número primo")
else:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(f"{n} é um número primo")
    else:
        print(f"{n} não é um número primo")