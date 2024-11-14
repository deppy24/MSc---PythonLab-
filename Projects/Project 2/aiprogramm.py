import csv
from datetime import datetime

# Αρχικό αρχείο CSV
FILENAME = 'tasks.csv'

# Συναρτήσεις
def init_csv():
    # Έλεγχος αν το αρχείο CSV υπάρχει, αν όχι το δημιουργεί με τα σωστά headers
    try:
        with open(FILENAME, 'x', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Ημερομηνία Εγγραφής', 'Α/α Εργασίας', 'Περιγραφή Εργασίας', 'Όνομα', 'Τηλέφωνο', 'Καταληκτική Ημερομηνία'])
    except FileExistsError:
        pass

def generate_task_id():
    # Δημιουργία μοναδικού αριθμού εργασίας
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Παράβλεψη του header
        tasks = [row for row in reader]
        
    return len(tasks) + 1

def add_task():
    task_id = generate_task_id()
    description = input("Περιγραφή εργασίας: ")
    name = input("Όνομα υπεύθυνου: ")
    phone = input("Τηλέφωνο: ")
    deadline = input("Καταληκτική ημερομηνία (YYYY-MM-DD): ")

    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILENAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([registration_date, task_id, description, name, phone, deadline])
    print("Η εργασία προστέθηκε με επιτυχία!")

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
    name = input(f"Όνομα υπεύθυνου ({task_to_modify[3]}): ") or task_to_modify[3]
    phone = input(f"Τηλέφωνο ({task_to_modify[4]}): ") or task_to_modify[4]
    deadline = input(f"Καταληκτική ημερομηνία ({task_to_modify[5]}): ") or task_to_modify[5]

    tasks.append([task_to_modify[0], task_id, description, name, phone, deadline])
    
    with open(FILENAME, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(tasks)

    print("Η εργασία ενημερώθηκε με επιτυχία!")

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

def display_all_tasks():
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            print(row)

def search_by_name():
    name = input("Εισάγετε το όνομα του υπεύθυνου: ")
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        print(header)
        for row in reader:
            if row[3].lower() == name.lower():
                print(row)

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

def alphabetical_list():
    from collections import Counter
    names = []
    with open(FILENAME, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Παράβλεψη header
        for row in reader:
            names.append(row[3])
    
    name_counts = Counter(names)
    for name, count in sorted(name_counts.items()):
        print(f"{name}: {count} εργασίες")

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
    init_csv()
    
    while True:
        print("\nΜενού:")
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