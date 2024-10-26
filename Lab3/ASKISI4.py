

# Διάβασμα του αριθμού από τον χρήστη
number = int(input("Εισάγετε θετικό ακέραιο αριθμό: "))

# Μετατροπή του αριθμού σε string για να μπορέσουμε να κάνουμε slicing
number_str = str(number)

# Υπολογισμός του αθροίσματος των ψηφίων
digit_sum = sum(int(digit) for digit in number_str)

# Έλεγχος αν ο αριθμός είναι Harshad
if number % digit_sum == 0:
    print(f"Ο αριθμός {number} είναι αριθμός Harshad.")
else:
    print(f"Ο αριθμός {number} δεν είναι αριθμός Harshad.")

#/////////
import random

# Generate a random number with a specific number of digits, for example, 5 digits
random_number = random.randint(10000, 99999)

# Convert the random number to a string to easily slice it
random_number_str = str(random_number)

# Initialize variables to hold each digit
digit1 = random_number_str[0]
digit2 = random_number_str[1]
digit3 = random_number_str[2]
digit4 = random_number_str[3]
digit5 = random_number_str[4]

# Print the results
print(f"Random Number: {random_number}")
print(f"Digits: {digit1}, {digit2}, {digit3}, {digit4}, {digit5}")