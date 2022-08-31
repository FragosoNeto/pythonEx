import random
import numpy
n=int(input('Quantos jogos você gostaria de fazer?'))
mt=numpy.zeros((n,6), dtype=numpy.int16)
for l in range(0,n):
    for c in range(0,6):
        mt[l][c] = random.randint(0, 60)
        if mt[l][c]==mt[l][5-c]:
            mt[l][c]*0

print(f'SORTEANDO {n} JOGOS')
for x in range(0,n):
    print(f'{x+1}º jogo: {mt[x]}')
