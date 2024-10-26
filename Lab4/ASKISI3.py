 
digit_dict = {
        '0': 'μηδέν',
        '1': 'ένα',
        '2': 'δύο',
        '3': 'τρία',
        '4': 'τέσσερα',
        '5': 'πέντε',
        '6': 'έξι',
        '7': 'επτά',
        '8': 'ογδόντα',
        '9': 'εννέα'
    }
phone_number = input("Εισάγετε έναν αριθμό τηλεφώνου: ")
verbal_number = []
for digit in phone_number:
        if digit in digit_dict:  # Έλεγχος αν το ψηφίο υπάρχει στο λεξικό
            verbal_number.append(digit_dict[digit])
        else:
            verbal_number.append(f"'{digit}' δεν είναι έγκυρο ψηφίο")
  
print(f"Ο αριθμός τηλεφώνου σε λεκτική μορφή είναι:{verbal_number}")



