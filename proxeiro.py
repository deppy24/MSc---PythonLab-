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

lista_katagrafwn=[]
    sum=0
    with open("ArxeioCsv.csv",'r',encoding='utf8') as arxeio:
        
        reader=csv.reader(arxeio)
        
        next(reader)
        for row in reader:
            if row[2] in uniquenumberset:
                #time_str=row[4]
                lista_katagrafwn.append((row[2],convert_time_to_seconds(row[4])))
            lista_telephone=Counter(num for num, xronos_klisis in lista_katagrafwn)  
        #max_count=Counter(lista_telephone)
    max_counter=max(lista_telephone.values(), default=0)
    max_emfanisi=[num for num,freq in lista_telephone.items() if freq==max_counter]
    print(lista_telephone,max_counter,max_emfanisi)
    if max_counter == 0:
        print("Καμία κλήση δεν βρέθηκε")
        return

