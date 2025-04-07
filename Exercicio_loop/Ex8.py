#Print dos números do 10 ao 1000 de 10 em 10
for i in range(10,1001):
    if i % 10 == 0:
        print(i)

#Print dos números do 15 ao 1000 de 10 em 10

for i in range(15,1001):
    if i % 5 == 0 and i % 10 != 0:
        print(i)