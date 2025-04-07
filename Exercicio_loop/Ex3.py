#Pedir a nota dos alunos
notas = []

for i in range(0, 10):
    n = int(input("Insira a nota dum aluno: "))
    notas.append(n)

#Cálculo da média
soma = sum(notas)
media = soma / len(notas)

print(f"A média das notas inseridas é: {media}")