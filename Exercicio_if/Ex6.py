#Pedido do nome do cliente e do valor da compra que vai fazer
nome = input("Digite o seu nome: ")
valor_compra = float(input("Digite o valor da sua compra: "))

#Verificar o valor do desconto da compra
if valor_compra <= 200:
    desconto_percentagem = 10
elif valor_compra <= 500:
    desconto_percentagem = 15
else:
    desconto_percentagem = 20

#Saber o valor que foi retirado da compra
valor_desconto = valor_compra * (desconto_percentagem / 100)

#Saber o valor final dessa compra
valor_final = valor_compra - valor_desconto

#Recibo da compra
print("\n--- Recibo ---")
print(f"Cliente: {nome}")
print(f"Valor da compra: €{valor_compra}")
print(f"Desconto: {desconto_percentagem}%")
print(f"Valor do desconto: €{valor_desconto}")
print(f"Total a pagar: €{valor_final}")