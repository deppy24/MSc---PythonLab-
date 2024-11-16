import csv,random,datetime,time
random.seed

#Πρόγραμμα διαχείρισης τηλεφωνικών επαφών και κλήσεων
print("Καλώς ήρθατε στο πρόγραμμα διαχείρισης τηλεφωνικών επαφών και κλήσεων ")

LexsikoOnomatwn = {
    '1':'Λυδία',
    '2':'Κωσταντίνα',
    '3':'Ορφέας',
    '4':'Γιάννης',
    '5':'Χαρά',
}
LexsikoEpithetwn = {
    '1':'Σκετέρη/ης',
    '2':'Γεωργιάδη',
    '3':'Καρβασίλη',
    '4':'Γόγγκου',
    '5':'Μπούσιου/ος',
}
def generate_telephone():
    firstdigit=69
    phonehumber=str(firstdigit)
    for i in range(8):
        phonehumber+= str(random.randint(0,9))
    return phonehumber

    return phonehumber
def generate_email(name):
    firstpart=str(name)
    emailtotal=name + "@gmail.com"
    return emailtotal
uniquenumberset=set()

#Δημιουργία Επαφές - Csv 1
with open("EpafesCsv.csv",'w',newline='',encoding='utf8') as epafes:
    
    writer = csv.writer(epafes)
    writer.writerow(['Όνομα','Επώνυμο','Τηλέφωνο','Email'])
    for egrafes10 in range(10):
        name=random.choice(list(LexsikoOnomatwn.values()))
        surname=random.choice(list(LexsikoEpithetwn.values()))
        telephone=generate_telephone()
        #Μοναδικός αριθμός τηλεφώνου
        while telephone in uniquenumberset:
            telephone = generate_telephone()
        uniquenumberset.add(telephone)
        email=generate_email(name)
        writer.writerow([name,surname,telephone,email])

def checktelephoneinput():
    while True:  
        telephone = input("Πληκτρoλόγησε τον αριθμό τηλεφώνου: ")
        try:
            if not telephone.isdigit() or len(telephone) != 10:
                print("Ο αριθμός τηλεφώνου πρέπει να είναι αυστηρά 10 ψηφία")
                continue
            if not telephone.startswith("69"):
                print("Ο αριθμός τηλεφώνου πρέπει να ξεκινάει με 69")
                continue
            break
        except ValueError:
            print("Ο αριθμός τηλεφώνου δέχεται μόνο ακέραιους αριθμητικούς χαρακτήρες")
    return telephone  

def add_new():
    with open("EpafesCsv.csv",'a',newline='',encoding='utf8') as epafes:
        writer=csv.writer(epafes)
        name=input("Πληκτρολόγησε το όνομα επαφής: ")
        surname=input("Πληκτρολόγησε το επώνυμο επαφής: ")
        telephone= checktelephoneinput()
        while telephone in uniquenumberset:
            telephone=checktelephoneinput()
        uniquenumberset.add(telephone)
        email=generate_email(name)
        writer.writerow([name,surname,telephone,email])
        print("Μία νέα επαφή εισάχθηκε επιτυχώς")
        time.sleep(1)

def metavoli_epafis():
    with open("EpafesCsv.csv",'r',newline='',encoding='utf8') as epafes:
        reader=csv.reader(epafes)
        #Γραφουμε τα δεδομενα του csv σε μια λίστα
        listepafes = [row for row in reader]
        telephone=checktelephoneinput()
        #Φτιάχνουμε μία νέα λίστα με την γραμμή όπου βρίσκεται ο αριθμος που εντοπίσαμε
        rows_with_value = [index for index, row in enumerate(listepafes) if telephone in row]
        found = False
        #Τσεκάρουμε αν υπάρχει στη λίστα με τα αποθηκευμένα τηλέφωνα επαφών
        if telephone in uniquenumberset:
            
            #Λαμβάνουμε τα νέα δεδομένα
            name=input(f"Εισάγεται νεό όνομα: ")
            surname=input(f"Εισάγεται νέο επώνυμο: ")
            print("Note: Ο αριθμός τηλεφώνου δεν μπορεί να μεταβληθεί \nΤο νέο email έχει δημιουργηθεί")
            email=generate_email(name)
            #telephone
            #Καταγράφουμε τα νέα δεδομένα
            new_row=[name,surname,telephone,email]
            #Τα περνάμε στον αριθμό σειράς που είχαμε βρει , για να μεταβάλουμε
            listepafes[rows_with_value[0]]=new_row
            found==True
        else: print("Δεν βρέθηκε")
    #Χρησιμοποιούμαι τη μεταβλητή True προκειμένου να διπλοτσεκάρουμε οτι βρέθηκε ο αριθμός 
    if found == True:    
        with open("EpafesCsv.csv",'w',newline='',encoding='utf8') as epafes:
            #Ξαναγράψιμο 
            epafes.seek(0)
            writer=csv.writer(epafes)
            writer.writerows(listepafes)
            epafes.truncate()
            print("Η επαφή μεταβλήθηκε επιτυχώς")
    else: print("Δεν βρέθηκε")

#Κύρια συνάρτηση ΄--Μενου Προγράμματος--
def main():
    
    while True:
        print("\n---Μενού---")
        print("1. Εισαγωγή επαφής")
        print("2. Μεταβολή επαφής")
        print("3. Διαγραφή επαφής")
        print("4. Κλήση Επαφής")
        print("5. Εμφάνιση κλήσεων επαφής (αναζήτηση με όνομα τηλέφωνο)")
        print("6. Εμφάνιση αλφαβητικής λίστας επαφών με πλήθος κλήσεων και συνολική διάρκεια ομιλίας")
        print("7. Εύρεση επαφής με περισσότερες κλήσεις")
        print("8. Εύρεση επαφής με συνολικά μεγαλύτερη διάρκεια ομιλίας")
        print("9. Έξοδος")
        
        time.sleep(2)
        choice = input("Επιλέξτε μια επιλογή: ")

        if choice == '1':
            add_new()
        
        elif choice == '2':
            metavoli_epafis()
        else:
            print("Μη έγκυρη επιλογή! Δοκιμάστε πάλι.")
        '''elif choice == '3':
            
        elif choice == '4':
            
        elif choice == '5':
            
        elif choice == '6':
            
        elif choice == '7':
            
        elif choice == '8':
            
        elif choice == '9':
            print("Το πρόγραμμα κλείνει")
            time.sleep(2)
            break'''
        

if __name__ == "__main__":
    main()