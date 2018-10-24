import sys
import random
listaGraczy = ['A','B','C','D','E','F','G','H','I','J']

def generujTeamy(lista):
    random.shuffle(lista)
    team2 = lista[0: len(lista) // 2]
    team1 = lista[len(lista) // 2:]
    return team1, team2
    
print (sys.argv[ 1: ])
a = generujTeamy( [1,2,3,4,5,6,7,8,9,0] )

print(a)