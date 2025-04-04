# Leitura das 10 notas
n1 = float(input("Digite a nota do aluno 1 (0 a 20): "))
n2 = float(input("Digite a nota do aluno 2 (0 a 20): "))
n3 = float(input("Digite a nota do aluno 3 (0 a 20): "))
n4 = float(input("Digite a nota do aluno 4 (0 a 20): "))
n5 = float(input("Digite a nota do aluno 5 (0 a 20): "))
n6 = float(input("Digite a nota do aluno 6 (0 a 20): "))
n7 = float(input("Digite a nota do aluno 7 (0 a 20): "))
n8 = float(input("Digite a nota do aluno 8 (0 a 20): "))
n9 = float(input("Digite a nota do aluno 9 (0 a 20): "))
n10 = float(input("Digite a nota do aluno 10 (0 a 20): "))

# Cálculo da média
media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10

# Verificação de quantos alunos ficaram com nota maior ou igual à média
contador = 0

if n1 >= media:
    contador += 1
if n2 >= media:
    contador += 1
if n3 >= media:
    contador += 1
if n4 >= media:
    contador += 1
if n5 >= media:
    contador += 1
if n6 >= media:
    contador += 1
if n7 >= media:
    contador += 1
if n8 >= media:
    contador += 1
if n9 >= media:
    contador += 1
if n10 >= media:
    contador += 1

# Apresentação dos resultados
print(f"\nMédia da turma: {media}")
print(f"Número de alunos com nota igual ou acima da média: {contador}")