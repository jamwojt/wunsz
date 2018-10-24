import random
listaGraczy = ['A','B','C','D','E','F','G','H','I','J']
team1 = []
team2 = []
for el in range( len (listaGraczy) ):
    losowyGracz = random.choice (listaGraczy)
    listaGraczy.remove(losowyGracz)
    team1.append(losowyGracz)
    
#random.shuffle(listaGraczy) (tak też można)

team2 = team1[0: len(team1) // 2]
team1 = team1[len(team1) // 2:]
print(team1)
print(team2)