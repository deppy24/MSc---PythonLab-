
#Initialization of variables
PrwthKlimaka = DeuteriKlimaka = TritiKlimaka = TetartiKlimaka =0

#Run the programm until the user interrupts it 
try: 
    while True:
        #Manage the input value
        try:
            EthsioEisodima = float(input("Εισάγεται το ετήσιο εισόδημα σας: "))
        except ValueError:
            print("Παρακαλώ εισάγεται μόνο πραγματικούς ή ακέραιους αριθμούς") 
            continue
        #Calculate the variables depending on the scale of your yearly salary
        if  EthsioEisodima < 10000:
            PrwthKlimaka = 0*100
            PosostoForou = PosoForou = PrwthKlimaka 
        elif 10001<EthsioEisodima<20000:
            DeuteriKlimaka = 0.1*100
            PosostoForou = DeuteriKlimaka
            PosoForou = 0.1 *(EthsioEisodima-10000) 
        elif 20001<EthsioEisodima<40000:
            TritiKlimaka = 0.2*100
            PosostoForou = DeuteriKlimaka + TritiKlimaka
            PosoForou = 0.1 *10000 + 0.2*(EthsioEisodima-20000)
        elif 40001<EthsioEisodima:
            TetartiKlimaka = 0.3*100
            PosostoForou = DeuteriKlimaka + TritiKlimaka + TetartiKlimaka
            PosoForou =  0.1 *10000 + 0.2*20000+ 0.3*(EthsioEisodima-40000)
        else:
            print("Ο υπολογισμός φόρου εισοδήματος δεν εκτελέστηκε")
        KatharoEisodima = EthsioEisodima - PosoForou
        print(f"Το συνολικό ποσού φόρου που υπολογίστηκε ειναι: {PosoForou:.2f}€ \nΤο συνολικό ποσοστό φόρου που υπολογίστηκε και κατανεμήθηκε ανάλογα ειναι: {PosostoForou:.2f}% \nΤο καθαρό εισόδημα που προκύπτει είναι: {KatharoEisodima:.2f}€")
except KeyboardInterrupt:
    print("\nΚαλή συνέχεια")

