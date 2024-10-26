    
import random
random.seed

erwtiseis_Dict={
    'Ποιά είναι η πρωτεύουσα της Ελλάδας;':'Αθήνα',
    'Είναι η Ελλάδα εντός της Ευρωζώνης;': 'Ναι',
    'Σε ποια Ήπειρο βρίσκεται η Μαδαγασκάρη;':'Αφρική',
    'Ανήκει η Κροατία στα Βαλκάνια;':'Ναι'
}


correct_count = wrong_count = 0

for erwtiseis in range(4):
    TrapezaErwtisewn=random.choice(list(erwtiseis_Dict.keys()))
    print(input(TrapezaErwtisewn ))
    if input in erwtiseis_Dict:
        print("CORRECT ANSWER")
        correct_count+=1
    else: 
        print("WRONG ANSWER") 
        wrong_count+=1

pososto_correct_count=(wrong_count/correct_count)*100 
pososto_wrong_count=(correct_count/wrong_count)*100
print(f'Correct answers: {correct_count}/5 with {pososto_correct_count}%. /fWrong answers: {wrong_count}/5 with {pososto_wrong_count}%')


