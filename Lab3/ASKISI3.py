
import random

def coin_toss_simulation(num_tosses):
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        toss = random.choice(['Head', 'Tail'])
        print(toss)
        
        if toss == 'Head':
            heads_count += 1
        else:
            tails_count += 1

    # Υπολογισμός ποσοστών
    heads_percentage = (heads_count / num_tosses) * 100
    tails_percentage = (tails_count / num_tosses) * 100

    print(f"\nΠοσοστά: \nHead: {heads_percentage:.2f}% \nTail: {tails_percentage:.2f}%")

def main():
    try:
        num_tosses = int(input("Εισάγετε τον αριθμό ρίψεων: "))
        if num_tosses <= 0:
            print("Παρακαλώ, εισάγετε έναν θετικό αριθμό.")
            return
        coin_toss_simulation(num_tosses)
    except ValueError:
        print("Παρακαλώ, εισάγετε έναν έγκυρο αριθμό.")

if __name__ == "__main__":
    main()