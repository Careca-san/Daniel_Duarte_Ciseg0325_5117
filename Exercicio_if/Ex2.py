#Pedido dos números
num1 = int(input("Por favor insira o primeiro número: "))
num2 = int(input("Por favor insira o segundo número: "))
num3 = int(input("Por favor insira o terceiro número: "))

#Verificar qual o maior e menor
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"Maior: {num1} e menor: {num3}")
    else:
        print(f"Maior: {num1} e menor: {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"Maior: {num2} e menor: {num3}")
    else:
        print(f"Maior: {num2} e menor: {num1}")
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f"Maior: {num3} e menor: {num2}")
    else:
        print(f"Maior: {num3} e menor: {num1}")
else:
    print("Por favor insira números diferentes")