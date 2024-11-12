
x = int(input("Πληκτρολογησε εναν ακεραιο αριθμο: "))



def Armstrong(x):
    metatropi =str(x)
    mikos=len(metatropi)
    sum=0
    for digit in metatropi:
        #To int digit μας δινει το περιεχομενο της {metatropi} για καθε digit δηλαδη για καθε επαναληψη
        sum += int(digit) ** mikos


        #Ελεγχει εαν η προταση ειναι αληθης και αυτο παραγει σαν αποτελεσμα (True of False)
        return sum==x
    

if Armstrong(x):
    print(f"O {x} ειναι αριθμος Armstrong")
else:
    print(f"O {x} δεν ειναι αριθμος Armstrong")