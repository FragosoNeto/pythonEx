#Fatorial de um número
print('##FATORIAL##')
n=int(input('ESCREVA UM NÚMERO:'))
cont=0
fat=1
for i in range(1,n+1):
   a=(n+1)-(cont+1)
   print(a)
   fat=fat*a
   cont = cont + 1



print(fat)