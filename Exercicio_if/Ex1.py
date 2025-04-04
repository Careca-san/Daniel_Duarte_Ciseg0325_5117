#Pedir o número de segundos
seg = int(input("Insira o número de segundos que quer converter: "))


horas = (seg/60)//60 #Cálculo de horas presentes nesse número de segundos
mins = (seg//60)-(horas*60) #Cálculo dos minutos excluindo todos os minutos que pertencem às horas calculadas
segs = seg - (mins*60) - ((horas*60)*60) #Cálculo dos segundos que é só tirar os das horas e dos minutos

#Resultado final
print(f"Convertendo daria {horas} horas, {mins} minutos e {segs} segundos") 