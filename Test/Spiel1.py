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

player = 1
avatar = "P"
#x = random.randint(4,12) # Länge des Felds
y = random.randint(3,8) # Breite des Felds
z = random.randint(0,5) # Typ der Wände
zz = random.randint(0,5) # Typ des Bodens
#g = random.randint(1,x) # Auf Welcher Linie die Nachricht geschrieben werden soll
position = 2


herp = [] # Speichert die nächste Zeile und gibt sie beim nächsten mal an
for i in range(0,y):
    herp += (" ") # Zum Initialisieren auf die richtige breite
    
# Code vom anderen Projekt genutzt für Ideen und richtigkeit
"""if ff > y: # Falls die Nachricht länger als die Breite wird, wird diese verlängert
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
    print(differentWalls(zz), end="")"""

print("Press a to move left and d to move right")
print(differentWalls(z), end="") # Start
for i in range(0,y):
    if (i+1) == position:
        print(avatar, end="")
    else:
        print(" ", end="")
print(differentWalls(z))

while player == 1: # Solange der Spieler lebt
    movement = input() # Ändere die Position um 1 Feld oder bei einem anderen Tastendruck gar nicht
    if movement == "a":
        position += -1
    elif movement == "d":
        position += 1
    if herp[(position-1)] != " ":
        player = 0
    else:
        herp[position] = avatar # Der Spieler nimmt die Stelle ein
    print(differentWalls(z), end="")
    for i in range(0,y):
        print(herp[i], end="")
    herp = [] # Liste wird geleert
    print(differentWalls(z))
    
    print(differentWalls(z), end="") # Nächste Ebene wird mitangezeigt
    for i in range(0,y):
        gh = random.randint(0,y)
        if i == gh:
            print(" ", end="")
            herp +=(" ") #Erste Ebene wird mit Daten gefüllt
        else:
            print(differentWalls(zz), end="")
            herp += (differentWalls(zz))
    print(differentWalls(z))
        
print("GAME OVER")
print("Du Kackspaßt")
