
N=(int(input("Δωσε ενα ακεραιο αριθμο: ")))
arithmitis=1
paranomastis=N

while N>1 and arithmitis<=N:
    akoloythia= arithmitis/N
    sum=+akoloythia
    arithmitis+=1
    paranomastis-=1
    print(f'Δείξε μου την ακολουθία που υπολογιζεται σε καθε επαναληψη {akoloythia} και το αθροισμα που προκυπτει με τις υπολοιπες {sum}')