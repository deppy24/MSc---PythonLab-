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

#Δημιουργία συναρτήσεων μενού
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
    #Τσεκάρουμε αν υπάρχει στη λίστα με τα αποθηκευμένα τηλέφωνα επαφών
    if rows_with_value:
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
        #Χρησιμοποιούμαι τη μεταβλητή True προκειμένου να διπλοτσεκάρουμε οτι βρέθηκε ο αριθμός 
           
        with open("EpafesCsv.csv",'w',newline='',encoding='utf8') as epafes:
            #Ξαναγράψιμο αρχείου
            writer=csv.writer(epafes)
            writer.writerows(listepafes)
            print("Η επαφή μεταβλήθηκε επιτυχώς")
    else: print("Δεν βρέθηκε")

def erase_epafis():
    with open("EpafesCsv.csv",'r',newline='',encoding='utf8') as epafes:
        reader=csv.reader(epafes)
        #Γραφουμε τα δεδομενα του csv σε μια λίστα
        listepafes = [row for row in reader]
    telephone=checktelephoneinput()
    #Φτιάχνουμε μία νέα λίστα με την γραμμή όπου βρίσκεται ο αριθμος που εντοπίσαμε
    rows_with_value = [index for index, row in enumerate(listepafes) if telephone in row]
    #Τσεκάρουμε αν υπάρχει στη λίστα με τα αποθηκευμένα τηλέφωνα επαφών
    if rows_with_value:
        #Διαγράφουμε τη σειρά εκείνη
        remove_row=listepafes.pop(rows_with_value[0])
        with open("EpafesCsv.csv",'w',newline='',encoding='utf8') as epafes:
            #Ξαναγράψιμο αρχείου
            writer=csv.writer(epafes)
            writer.writerows(listepafes)
            print("Η επαφή διαγράφηκε επιτυχώς")
    else: print("Δεν βρέθηκε")


lista_anapantitwn=[]
lista_pragmatopoimenwn=[]
lista_xronwn_klisewn=[]
def generate_duration_phonecall():
    min_duration=1
    #Μεγιστος χρονος κλησης 1 ωρα, θελουμε το input σε δευτερολεπτα
    max_duration=3600
    duration=random.randint(min_duration,max_duration)
    print (duration)
    #Μετατρεπουμε τον χρονο σε λεπτα και δευτερολεπτα
    minutes,seconds=divmod(duration,60)
    final=(f"{minutes}:{seconds}")
    return final
def klisi_epafis():
    with open("EpafesCsv.csv",'r',newline='',encoding='utf8') as epafes:
        reader=csv.reader(epafes)
        #Γραφουμε τα δεδομενα του csv σε μια λίστα
        listepafes = [row for row in reader]
    telephone=checktelephoneinput()
    #Φτιάχνουμε μία νέα λίστα με την γραμμή όπου βρίσκεται ο αριθμος που εντοπίσαμε
    rows_with_value = [index for index, row in enumerate(listepafes) if telephone in row]
    if rows_with_value:
        #Επιλέγει τυχαία εάν η κλήση θα ειναι αναπαντητη η πραγματοποιημενη
        k=random.choice(list(["Αναπάντητη", "Πραγματοποιημένη"]))
        xronos_klisis=0
        if k=="Αναπάντητη": 
            xronos_klisis='0:0'
            count = sum(1 for k_ in k if k == "Αναπάντητη")
            lista_anapantitwn=[count]
        elif k=='Πραγματοποιημένη':
            xronos_klisis=generate_duration_phonecall()
            count = sum(1 for k_ in k if k == "Πραγματοποιημένη")
            lista_pragmatopoimenwn=[count]
            lista_xronwn_klisewn=[xronos_klisis]
        imerominia=datetime.date.today()
        wra=datetime.datetime.now().time()
        new_row=[imerominia,wra,telephone,k,xronos_klisis]
        print("Η κλήση ολοκληρώθηκε")
        with open("ArxeioCsv.csv",'a',newline='',encoding='utf8') as arxeio:
            #Ξαναγράψιμο αρχείου
            writer=csv.writer(arxeio)
            if arxeio.tell() == 0:  # Check if file is empty
                writer = csv.writer(arxeio)
                writer.writerow(['Ημερομηνία', 'Ώρα','Αριθμός επαφής', 'Περιγραφή κλήσης', 'Διάρκεια'])
            writer.writerow(new_row)
            print("Η κλήση καταγράφηκε επιτυχώς")
    else:print("Δεν βρέθηκε")

def emfanisi():
    i=0
    telephone=checktelephoneinput()
    with open("ArxeioCsv.csv",'r',newline='',encoding='utf8') as arxeio:
        reader = csv.reader(arxeio)
        for row in arxeio:
            if telephone in row:
                print(row)
                i+=1
    if i==0:print("Δεν βρέθηκε στο αρχείο κλήσεων")


def convert_time_to_seconds(time_str):
    #Το πεδιο time: mm:ss το σπαμε σε δυο και το μετατρεπουμε σε ακεραιο
    minutes_str, seconds_str= time_str.split(':')
    minutes = int(minutes_str)
    seconds = int(seconds_str)
    
    #Μτατρεπουμε σε συνολικα δευτερολεπτα
    total_seconds = (minutes * 60) + seconds
    return total_seconds
def search_max_duration():
    lista_katagrafwn = []  # List to hold call records
    with open("ArxeioCsv.csv", 'r', encoding='utf8') as arxeio:
        reader = csv.reader(arxeio)
        next(reader)  
        
        for row in reader:
            # Ελεγχος αν ο αριθμος που βρισκει υπαρχει μεσα στο uniquenumberset που εχει οριστει πιο πανω
            if row[2] in uniquenumberset:
                try:
                    duration = convert_time_to_seconds(row[4])
                    #Δημιουργια μιας λιστας με τα τηλεφωνα που εχουν γινει κλησεις και τις διαρκειες τους
                    lista_katagrafwn.append((row[2], duration))
                except ValueError:
                    print(f"Error converting time for row: {row}")

    #Δημιουργία λιστας για τον αριθμο εμφανισης των τηλεφωνων στις κλησεις 
    lista_telephone = Counter(num for num, duration in lista_katagrafwn)
    #Ευρεση μεγιστου αριθμου εμφανισης τηλεφωνου στις κλησεις  
    max_counter = max(lista_telephone.values(), default=0)
    #Ευρεση αριθμου/αριθμων με την μεγιστη εμφανιση στο αρχειο κλησεων 
    max_emfanisi = [num for num, freq in lista_telephone.items() if freq == max_counter]
      
    if max_counter == 0:
        print("Καμία κλήση δεν βρέθηκε")
        return
       
    total_durations = {num: 0 for num in max_emfanisi}
    for num, duration in lista_katagrafwn:
        if num in max_emfanisi:
            #Ευρεση συνολικης διαρκειας κλησεις για τους αριθμους που βρεθηκαν με μεγιστο αριθμο εμφανισης στο αρχειο κλησεων
            total_durations[num] += duration  
    if len(max_emfanisi) == 1:
        print(f"Μεγαλύτερη συχνότητα κλήσεων παρατηρήθηκε στην επαφή με αριθμό: {int(max_emfanisi[0])} με {max_counter} κλήσεις και συνολική διάρκεια {total_durations[max_emfanisi[0]]} δευτερολέπτων")
    else:
        details = ", ".join(f"{num}: {total_durations[num]} δευτερολέπτων" for num in max_emfanisi)
        print(f"Μεγαλύτερη συχνότητα κλήσεων παρατηρήθηκε στις επαφές με τους αριθμούς: {', '.join(map(str, max_emfanisi))} με {max_counter} κλήσεις έκαστος και Συνολικές διάρκειες \n{details}")

from collections import Counter
def search_max_kliseis():
    lista_katagrafwn=[]
    with open("ArxeioCsv.csv",'r',encoding='utf8') as arxeio:
        reader=csv.reader(arxeio)
        for row in reader:
            if row[2] in uniquenumberset:
                lista_katagrafwn.append(row[2])
    max_count=Counter(lista_katagrafwn)
    max_counter=max(max_count.values(), default=0)
    max_emfanisi=[num for num,freq in max_count.items() if freq==max_counter]
    if max_counter == 0:
        print("Καμία κλήση δεν βρέθηκε")
    elif max_counter == 1:
        if len(max_emfanisi) == 1:
            print(f"Μεγαλύτερη συχνότητα κλήσεων παρατηρήθηκε στην επαφή με αριθμό: {int(max_emfanisi[0])} με {max_counter} κλήση")
        else:
            print(f"Μεγαλύτερη συχνότητα κλήσεων παρατηρήθηκε στις επαφές με τους αριθμούς: {int(max_emfanisi)} με {max_counter} κλήσεις")
    else:
        print(f"Μεγαλύτερη συχνότητα κλήσεων παρατηρήθηκε στις επαφές με τους αριθμούς: {int(max_emfanisi)} με {max_counter} κλήσεις αντίστοιχα")


def alphabetical():
    kontakts_info = {}
    
    # Read the call records to gather information on calls and durations
    with open("ArxeioCsv.csv", 'r', encoding='utf8') as arxeio:
        reader = csv.reader(arxeio)
        next(reader)  
        
        for row in reader:
            telephone = row[2]  # Contact number
            call_type = row[3]  # Call description (not used for this task)
            duration_str = row[4]  # Duration
            
            #Μετατροπη χρονου κλησης σε δευτερολεπτα
            duration_seconds = convert_time_to_seconds(duration_str)
            
            # Πληροφορια για καθε τηλεφωνο
            if telephone in kontakts_info:
                kontakts_info[telephone]['calls'] += 1
                kontakts_info[telephone]['total_duration'] += duration_seconds
            else:
                kontakts_info[telephone] = {'calls': 1, 'total_duration': duration_seconds}
    contacts = []
    with open("EpafesCsv.csv", 'r', encoding='utf8') as epafes:
        reader = csv.reader(epafes)
        next(reader)  
        
        for row in reader:
            name = row[0]  # Όνομα
            surname = row[1]  #Επώνυμο
            telephone = row[2]  #Τηλέφωνο
            contacts.append((name, surname, telephone))

    # Sorting με βαση το ονομα
    contacts.sort()

    print("\n--- Αλφαβητική Λίστα Επαφών ---")
    for name, surname, telephone in contacts:
        if telephone in kontakts_info:
            count_calls = kontakts_info[telephone]['calls']
            total_duration = kontakts_info[telephone]['total_duration']
            # Μετατροπη χρονου κλησης ξανα σε format mm:ss 
            minutes, seconds = divmod(total_duration, 60)
            duration_display = f"{minutes}:{seconds:02}"
            print(f"{name} {surname}, Τηλέφωνο: {telephone}, Πλήθος Κλήσεων: {count_calls}, Συνολική Διάρκεια: {duration_display}")
        else:
            print(f"{name} {surname}, Τηλέφωνο: {telephone}, Πλήθος Κλήσεων: 0, Συνολική Διάρκεια: 0:00")

#Κύρια συνάρτηση ΄--Μενου Προγράμματος--
def main():
    
    while True:
        print("\n---Μενού---")
        print("1. Εισαγωγή επαφής")
        print("2. Μεταβολή επαφής")
        print("3. Διαγραφή επαφής")
        print("4. Κλήση Επαφής")
        print("5. Εμφάνιση κλήσεων επαφής (αναζήτηση με τηλέφωνο)")
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
        elif choice == '3':
            erase_epafis()
        elif choice == '4':
            klisi_epafis()
        elif choice == '5':
            emfanisi()
        elif choice == '6':
            alphabetical()
        elif choice == '7':
            search_max_kliseis()
        elif choice == '8':
            search_max_duration()
        elif choice == '9':
            print("Το πρόγραμμα κλείνει")
            time.sleep(2)
            break
        else:
            print("Μη έγκυρη επιλογή! Δοκιμάστε πάλι.") 


main()
