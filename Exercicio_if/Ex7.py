#Pedido das notas das provas
nota1 = float(input("Digite a nota da primeira prova (0 a 10): "))
nota2 = float(input("Digite a nota da segunda prova (0 a 10): "))
nota3 = float(input("Digite a nota da terceira prova (0 a 10): "))

#Definição dos pesos das provas
peso1 = 2
peso2 = 3
peso3 = 5

#Cálculo da média
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

#Verificação para saber se foi aprovado ou não
if media >= 6:
    print(f"Média final: {media} - APROVADO")
else:
    print(f"Média final: {media} - REPROVADO")