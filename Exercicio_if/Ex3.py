#Pedido dos números
num1 = int(input("Insira um número à escolha: "))
num2 = int(input("Insira outro número à escolha: "))

#Comparação entre eles
if num1 == num2:
    print("Por favor, insira números diferentes um do outro")
elif num1 < num2:
    print(f"Números por ordem crescente: {num1} e {num2} \n Números por ordem decrescente: {num2} e {num1}")    
else:
    print(f"Números por ordem crescente: {num2} e {num1} \n Números por ordem decrescente: {num1} e {num2}")