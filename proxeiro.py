#Η ΦΟΡ ΙΝ ΣΑΡΩΝΕΙ ΤΙΣ ΑΛΦΑΡΙΘΜΗΤΙΚΕΣ ΜΕΤΑΒΛΗΤΕΣ ΜΙΑ ΠΡΟΣ ΜΙΑ ΓΙΑ ΑΥΤΟ ΤΑ ΕΜΦΑΝΙΖΕΙ ΚΑΘΕΤΑΙ ΕΝΑ ΕΝΑ
#ΚΑΘΕ ΧΑΡΑΚΤΗΡΑΣ ΕΙΝΑΙ ΜΙΑ ΕΠΑΝΑΛΗΨΗ
#str="dyi"
#for value in str :
   #print(value)


#ΣΕ ΑΥΤΗΝ ΤΗΝ ΠΕΡΙΠΤΩΣΗ ΤΟ ΒΑΛΙΟΥ ΠΕΡΝΕΙ ΤΗΝ ΣΤΑΡΤ ΤΙΜΗ ΤΗΣ ΡΕΙΝΤΖ ΚΑΙ ΜΠΟΡΕΙ ΝΑ ΧΡΗΣΙΜΟΠΟΙΗΘΕΙ ΣΑΝ ΜΕΤΑΒΛΗΤΗ 
#for value in range(100,200,3):
    #print(value)

#ΔΗΜΙΟΥΡΓΙΑ ΠΙΝΑΚΑ 4Χ4
'''import random
print('Array 4x4 with random values:')
Α = [[random.randint(0,9) for x in range(4)] for x in range(4)]
for i in range(len(Α)):
    for j in range(len(Α[0])):
        print('%3d' % Α[i][j], end="")
    print()'''

import random
'''def randomDice():
    return random.randint(1, 6)
print (randomDice())'''

def randomDice():
    k=random.radint(1,6)
    print (k)
    return
