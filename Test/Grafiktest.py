import random

def differentWalls(difWall):
    if difWall == 1:
        return "@"
    elif difWall == 2:
        return "#"
    elif difWall == 3:
        return "%"
    elif difWall == 4:
        return "!"
    elif difWall == 5:
        return "*"
    elif difWall == 0:
        return "Ö"

x = random.randint(4,12) # Länge des Felds
y = random.randint(10,50) # Breite des Felds
z = random.randint(0,5) # Typ der Wände
zz = random.randint(0,5) # Typ des Bodens
g = random.randint(1,x) # Auf Welcher Linie die Nachricht geschrieben werden soll

print("Enter a line")

line = str(input())
ff = len(line)

if ff > y: # Falls die Nachricht länger als die Breite wird, wird diese verlängert
    y += ff 
k = y-ff+1 # Breite des Feldes in dem die Nachricht angezeigt wird
j = random.randint(0,k) # An welcher Stelle die Nachricht auf der Linie angezeigt wird

for i in range(0,x):
    print(differentWalls(z), end="")
    if (i+1) == g:
        for i in range(0,k):
            if (i+1) == j:
                print(line, end="")
            else:
                print(" ", end="")
    
    else:
        for i in range(0,y):
            print(" ", end="")
    print(differentWalls(z))
for i in range(0,(y+2)):
    print(differentWalls(zz), end="")
