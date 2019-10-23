#! python3.7

# gerEngVocabularTrainer - A simple german - englisch vocabular training program

import random

vocabular = {"foundation": "Grundlage", "company": "Unternehmen", "profile": "Porträt"}

print("Please insert how many vocable's you want to learn")
howManyToLearn = int(input("Amount:"))

for i in range(1, howManyToLearn + 1):
    print(random.randint(1, len(vocabular)))
    
