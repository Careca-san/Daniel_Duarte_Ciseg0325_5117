# Começa no código ASCII 0
codigo = 0

# Loop até 255
while codigo <= 255:
    # Mostra 20 códigos por página
    for i in range(20):
        if codigo > 255:
            break
        try:
            # Print do código e o caractere correspondente
            print(f"Código: {codigo:3}  ->  Carácter: {chr(codigo)}")
        except:
            # Alguns códigos podem não ter representação visível
            print(f"Código: {codigo:3}  ->  Carácter: <inválido>")
        codigo += 1

    # Pergunta ao utilizador se quer continuar
    opcao = input("\nPrima ENTER para continuar ou escreva 'sair' para terminar: ")
    if opcao.lower() == "sair":
        break