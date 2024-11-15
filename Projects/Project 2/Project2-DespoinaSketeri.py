import csv
from datetime import datetime,timedelta
import random
random.seed
# Αρχικό αρχείο CSV
FILENAME = 'tasks.csv'

#Στοιχεια για την εισαγωγη των πρωτων 10 γραμμων
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
#Συναρτήσεις για ελέγχους
def generate_random_phone_number():
    # Δημιουργία ενός αριθμού τηλεφώνου 
    first_digit = 69
    phone_number = f"{first_digit}"
    # Δημιουργία υπολοιπου αριθμου
    for _ in range(8):
        phone_number += str(random.randint(0, 9))
    return phone_number
def number_input():
    number = input("Εισάγετε αριθμό τηλεφώνου: ")

    try:
        # Έλεγχος αν ο αριθμός είναι 10 ψηφία
        if len(number) != 10:
            raise ValueError("Ο αριθμός τηλεφώνου πρέπει να έχει 10 ψηφία.")
        
        # Έλεγχος αν περιέχει μόνο ψηφία
        if not number.isdigit():
            raise ValueError("Ο αριθμός τηλεφώνου πρέπει να περιέχει μόνο ψηφία.")
            
        print(f"Ο αριθμός τηλεφώνου {number} είναι έγκυρος.")
        number=generate_random_phone_number
    except ValueError as e:
        print(f"Σφάλμα: {e}")
def onoma_input():
    try:
        name = input("Εισάγετε όνομα: ")
        if name.isdigit() == True:
            raise Exception("Στα ονόματα το πρόγραμμα δέχεται μόνο γράμματα")
    except Exception as OnlyAlphas:
        print(f"Σφάλμα: {OnlyAlphas}")
    name=random.choice(list(LexsikoOnomatwn.values()))
def generate_task_id():
    # Δημιουργία μοναδικού αριθμού εργασίας
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        tasks = [row for row in reader]
        
    return len(tasks) + 1        


    
# Κάθε φορά που το πρόγραμμα τρέχει διαγράφει τα δεδομένα του και ξαναδημιουργέι τις σειρές με τυχαίους συνδιασμούς
#Εάν το αρχείο δεν υπάρχει , το δημιουργεί 
with open(FILENAME, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Ημερομηνία Εγγραφής', 'Α/α Εργασίας', 'Περιγραφή Εργασίας', 'Όνομα', 'Τηλέφωνο', 'Καταληκτική Ημερομηνία'])         
    for First10Row in range(10):
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_id = random.randrange(1000000)
        name = random.choice(list(LexsikoOnomatwn.values()))
        description = random.choice(list(LexsikoPerigrafis.values()))
        phone = generate_random_phone_number()
        today=datetime.now()
        deadline = today + timedelta(days=1)
        writer.writerow([registration_date, task_id, description, name, phone, deadline])




 
#-1-1 Συναρτησεις - Λειτουργιες Μενου
#Προσθηκη Εργασιας
def add_task():
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_id = generate_task_id()
    description = input("Περιγραφή εργασίας: ")
    name = onoma_input()
    phone = number_input()
    deadline = input("Καταληκτική ημερομηνία (YYYY-MM-DD): ")
    
    
    with open(FILENAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([registration_date, task_id, description, name, phone, deadline])
    print("Η εργασία προστέθηκε με επιτυχία!")

#Μεταβολή Εργασίας
def modify_task():
    task_id = input("Εισάγετε τον Α/α Εργασίας για μεταβολή: ")
    
    tasks = []
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        tasks = [row for row in reader if row[1] != task_id]
    
    if len(tasks) == len(header):
        print("Η εργασία δεν βρέθηκε.")
        return

    task_to_modify = None
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == task_id:
                task_to_modify = row
                break

    print("Τρέχουσες λεπτομέρειες της εργασίας:", task_to_modify)
    print("Νέα στοιχεία (πατήστε Enter για να διατηρήσετε την τρέχουσα τιμή):")

    description = input(f"Περιγραφή εργασίας ({task_to_modify[2]}): ") or task_to_modify[2]
    name = onoma_input()
    #phone = input(f"Τηλέφωνο ({task_to_modify[4]}): ") or task_to_modify[4]
    phone = number_input() 
    deadline = input(f"Καταληκτική ημερομηνία ({task_to_modify[5]}): ") or task_to_modify[5]

    tasks.append([task_to_modify[0], task_id, description, name, phone, deadline])
    
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(tasks)

    print("Η εργασία ενημερώθηκε με επιτυχία!")

#Διαγραφή Εργασίας
def delete_task():
    task_id = input("Εισάγετε τον Α/α Εργασίας για διαγραφή: ")
    
    tasks = []
    deleted = False
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        tasks = [row for row in reader if row[1] != task_id]
        if len(tasks) < len(header):
            deleted = True

    if deleted:
        with open(FILENAME, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(tasks)
        print("Η εργασία διαγράφηκε με επιτυχία!")
    else:
        print("Η εργασία δεν βρέθηκε.")

#Προβολή όλων
def display_all_tasks():
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            print(row)

#Αναζήτηση με όνομα
def search_by_name():
    #name = input("Εισάγετε το όνομα του υπεύθυνου: ")
    onoma_input()
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            if row[3].lower() == name.lower():
                print(row)
            else : print("Δεν βρέθηκε κάποια εργασία")
#Αναζήτηση με ημερομηνία
def search_by_date():
    date_str = input("Εισάγετε ημερομηνία (YYYY-MM-DD): ")
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            registration_date = row[0].split()[0]  # Μόνο η ημερομηνία χωρίς ώρα
            if registration_date == date_str:
                print(row)

#Αλφαβητική ταξινόνηση
def alphabetical_list():
    from collections import Counter
    names = []
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            names.append(row[3])
    
    name_counts = Counter(names)
    for name, count in sorted(name_counts.items()):
        print(f"{name}: {count} εργασίες")

#Max Εργασίες
def person_with_most_tasks():
    from collections import Counter
    names = []
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Παράβλεψη header
        for row in reader:
            names.append(row[3])
    
    name_counts = Counter(names)
    most_common = name_counts.most_common(1)
    if most_common:
        print(f"Το άτομο με τις περισσότερες εργασίες: {most_common[0][0]} - {most_common[0][1]} εργασίες")
    else:
        print("Δεν υπάρχουν εργασίες.")

def main():
    #init_csv()
    
    while True:
        print("\n---Μενού---")
        print("1. Εισαγωγή νέας εργασίας")
        print("2. Μεταβολή εργασίας")
        print("3. Διαγραφή εργασίας")
        print("4. Προβολή λίστας εργασιών (όλες)")
        print("5. Προβολή λίστας εργασιών (αναζήτηση με όνομα υπεύθυνου)")
        print("6. Προβολή λίστας εργασιών (αναζήτηση με ημερομηνία)")
        print("7. Εμφάνιση αλφαβητικής λίστας ονομάτων με πλήθος εργασιών")
        print("8. Εύρεση ατόμου με τις περισσότερες εργασίες")
        print("9. Έξοδος")
        
        choice = input("Επιλέξτε μια επιλογή: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            modify_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            display_all_tasks()
        elif choice == '5':
            search_by_name()
        elif choice == '6':
            search_by_date()
        elif choice == '7':
            alphabetical_list()
        elif choice == '8':
            person_with_most_tasks()
        elif choice == '9':
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή! Δοκιμάστε πάλι.")

if __name__ == "__main__":
    main()