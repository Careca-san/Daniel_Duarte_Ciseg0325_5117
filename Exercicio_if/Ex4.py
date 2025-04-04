#Saldo inicial do cliente
saldo = float(input("Digite o o seu saldo inicial: "))

#Valor do cheque a ser descontado
cheque = float(input("Digite o valor do cheque: "))

#Transação
if cheque > saldo:
    print("O cheque não pode ser descontado. Saldo insuficiente.")
else:
    saldo -= cheque
    print("Cheque descontado com sucesso.")
    print(f"Saldo actual: €{saldo}")