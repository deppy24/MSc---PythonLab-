import random

# Λίστα με ονόματα και επώνυμα
names = ["Γιώργος Παπαδόπουλος", "Μαρία Ιωαννίδου", "Αλέξανδρος Κωνσταντίνου", "Ελένη Νικολαΐδου", "Δημήτρης Χατζηγεωργίου"]

# Επιλογή τυχαίου ονόματος και επωνύμου
random_name = random.choice(names)

# Διαστάσεις παραλληλογράμμου
width = 20
height = 10

# Διαλέγουμε μια τυχαία γραμμή για το όνομα
name_line = random.randint(1, height - 2) # κρατάμε 1 και 8 για την περιφέρεια

# Δημιουργία του παραλληλογράμμου
for row in range(height):
    if row == 0 or row == height - 1:
        print('█' * width)  # Οριζόντιες γραμμές
    elif row == name_line:
        # Προσθέτουμε το όνομα σε στοίχιση κεντρικά
        name_position = (width - len(random_name)) // 2
        print('█' + ' ' * (name_position - 1) + random_name + ' ' * (width - name_position - len(random_name) - 1) + '█')
    else:
        print('█' + ' ' * (width - 2) + '█')  # Κενές γραμμές