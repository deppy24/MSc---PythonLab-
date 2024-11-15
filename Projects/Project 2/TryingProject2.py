
import datetime,csv,time,random 
random.seed

print("Καλώς ήρθες στο πρόγραμμα διαχείρισης εργασιών")
time.sleep(2)

#Στοιχεια που θα περιεχει το προγραμμα 
LexsikoPerigrafis = {
    '1':'Δημιουργία προγράμματος σε γλώσσα python',
    '2':'Έπίλυση αλγορίθμου βελτιστοιποίησης',
    '3':'Μελέτη αλγορίθμου μυρμηγκιών',
    '4':'Εύρεση ιστορικών πληροφοριών για την γλώσσα Java',
    '5':'Εύρεση παραδειγμάτων εφαρμογής της Java',
    '6':'Κατηγοροιοποίηση μαθηματικών προβλημάτων',
    '7':'Αξιολόγηση γραπτών',
    '8':'Ερευνητική εργασία',
    '9':'Εργαστηριακή εργασία',
    '10':'Πειραματική εργασία',
}
LexsikoOnomatwn = {
    '1':'Λυδία',
    '2':'Κωσταντίνα',
    '3':'Ορφέας',
    '4':'Γιάννης',
    '5':'Χαρά',
    '6':'Αιμιλία',
    '7':'Νικολέτα',
    '8':'Χάρης',
    '9':'Γιώργος',
    '10':'Αριάδνη',
}

'''for digits9 in range(9):
    Digits=random.randrange(0,9)
    ArithmosThlefwnoy = 69 + Digits
    print(ArithmosThlefwnoy)'''


'''

Thlefwno=int(input("Πληκτρολογηστε το τηλεφωνο σας: "))
TelikiHmero =(input("Εισάγεται την τελική ημερομηνία παράδοσης της εργασιας: "))'''

#Ορισμός αρχείου και εισαγωγή πρώτων γραμμών
with open('DiaxeiriErgasiwn.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['WorkDate', 'WorkId', 'Name', 'Perigrafi'])

    #Εισαγωγη 10 εργασιων με κωδικα
    for First10Row in range(10):
        WorkDate=datetime.date.today()
        WorkId = random.randrange(1000000)
        Name = random.choice(list(LexsikoOnomatwn.values()))
        Perigrafi = random.choice(list(LexsikoPerigrafis.values()))
        data =[WorkDate,WorkId,Name,Perigrafi]
        writer.writerow(data)

#Ορισμός συναρτήσεων : 1 Συνάρτηση - 1 Λειτουργία menu
#Εισαγωγή νέας εργασίας
def InsertNew():
    PerigrafiNew = input("Περιγράψτε την εργασία σας: ")
    NameNew= input("Πληκτρολογήστε το όνομα σας: ")
    WorkId = random.randrange(1000000)
    WorkDate = datetime.date.today()
    with open('DiaxeiriErgasiwn.csv','a') as f:
        writer = csv.writer(f)
        data =[WorkDate,WorkId,NameNew,PerigrafiNew]
        #Γράφει τα στοιχεία στο αρχείο
        writer.writerow(data)
        return print("Μία επιπλέον εργασία προστέθηκε επιτυχώς")
    time.sleep(2)

#Μεταβολή εργασίας
def ChangeErgasia(GiveID):
    found = False
    with open('DiaxeiriErgasiwn.csv','r') as f:
        
        for line in f:
            if str(GiveID) in line:
                found = True 
                PerigrafiNew = input("Περιγράψτε την εργασία σας: ")
                NameNew = input("Πληκτρολογήστε το όνομα σας: ")
                newrows=[GiveID,PerigrafiNew,NameNew]
                line = writer.writerows(newrows)
                     
    '''if found:
        with open('DiaxeiriErgasiwn.csv', 'a') as f:
        writer = csv.writer(f)        
    else:
        print("Αυτό το Id δεν αντιστοιχεί σε κάποια εργασία")   '''

def EraseErgasia(GiveID):
    with open('DiaxeiriErgasiwn.csv','r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row != GiveID]
    
def OpenErgasies():
    with open('DiaxeiriErgasiwn.csv','r') as f:
        all = f.read()
        print(all)
def OpenErgasia2(GiveName):
   with open('DiaxeiriErgasiwn.csv','r') as f:
        for line in f:
            if GiveName in line:
                 print(f.read(line))
            else: print(f"{GiveName} δεν βρέθηκε στο αρχείο")
def OpenErgasia3(GivenDate): 
    with open('DiaxeiriErgasiwn.csv','r') as f:
        for line in f:
            if GivenDate in line:
                 return print(f.read(line))
            else: return print(f"{GivenDate} δεν βρέθηκε στο αρχείο")
def Ergasia4():
    with open('DiaxeiriErgasiwn.csv','r') as f:
        lines = f.readlines()
        # Δημιουργία μιας λίστας για τη στήλη που θέλουμε
        lista = []
        for line in lines[1:]:  # Παράλειψη της πρώτης γραμμής (ονομάτων στήλης)
         parts = line.strip().split(',')
            # Προσθέτουμε το στοιχείο της στήλης στη λίστα
        if len(parts) > 0:  # Έλεγχος για να αποφευχθούν άδειες γραμμές
            lista.append(parts[2])  # Αντικαταστήστε το 0 με το δείκτη της επιθυμητής στήλης
    print(lista)
def MaxErgasia():
    with open('DiaxeiriErgasiwn.csv','r') as f:
        f.readline()
    # Δημιουργία ενός λεξικού για να μετρήσουμε τις εργασίες
        ergasies = {}
        for line in f:
        # Αφαιρούμε τα περιττά κενά και χωρίζουμε τη γραμμή με κόμμα
            Name = line.strip().split(',')
        # Αυξάνουμε τον μετρητή για το συγκεκριμένο όνομα
            if Name in ergasies:
                ergasies[Name] += 1
            else:
                ergasies[Name] = 1
    άτομο_max = max(ergasies, key=ergasies.get)
    max_εργασίες = ergasies[άτομο_max]
    return(f'Το άτομο με τις περισσότερες εργασίες είναι ο/η {άτομο_max} με {max_εργασίες} εργασίες.')  
def CloseErgasia():
    print("Το προγραμμα κλείνει...")
    time.sleep(2)
    exit()



try:
    while True:
        print("\n---Μενού Εργασιών--- \n1.Προσθήκη Εργασίας \n2.Μεταβολή Εργασίας \n3.Διαγραφή Εργασίας \n4.Προβολή λίστας Εργασιών \n5.Προβολή λίστας εργασιών (αναζήτηση με όνομα υπεύθυνου) \n6.Προβολή λίστας εργασιών (αναζήτηση με ημερομηνία) \n7.Εμφάνιση αλφαβητικής λίστας ονομάτων με πλήθος εργασιών \n8.Εύρεση ατόμου με τις περισσότερες εργασίες \n9.Έξοδος")
        time.sleep(2)
        x = input("\nΕπέλεξε απο το μενου πληκτρολογωντας τον αντιστοιχο αριθμο: ")
        if x=="1":
            InsertNew()
        elif x=="2":
            GiveID2=input("Ποιο ειναι το αναγνωστικο της εργασίας που θέλεις να αλλαξεις;")
            ChangeErgasia(GiveID2)
        elif x=="3":
            GiveID=input("Δωσε το id της εργασιας που θες να διαγραψεις: ")
            EraseErgasia(GiveID)
        elif x=="4":
            OpenErgasies()
        elif x=="5":
            GiveName = input("Πληκτρολόγησε το όνομα υπεύθυνου")
            OpenErgasia2(GiveName)
        elif x=="6":
            GivenDate = input("Εισαγωγή ημερομηνίας: ")
            OpenErgasia3(GivenDate)
        elif x=="7":
            Ergasia4()
        elif x=="8":
            MaxErgasia()
        elif x=="9":
            CloseErgasia()
except KeyboardInterrupt:
    print("\nΚαλή συνέχεια")


