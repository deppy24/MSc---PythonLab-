    
import random
random.seed
#Bank of questions , 10 in total
erwtiseis_Dict={
    'Ποιά είναι η πρωτεύουσα της Ελλάδας;':'Αθήνα',
    'Είναι η Ελλάδα εντός της Ευρωζώνης;': 'Ναι',
    'Σε ποια Ήπειρο βρίσκεται η Μαδαγασκάρη;':'Αφρική',
    'Ανήκει η Κροατία στα Βαλκάνια;':'Ναι',
    'Ποιο είναι το μεγαλύτερο νησί της Ελλάδας;': 'Κρήτη',
    'Ποιο είναι το εθνικό ποτό της Σκωτίας;': 'Ουίσκι',
    'Ποιό είναι το πιο ψηλό βουνό του κόσμου;': 'Έβερεστ',
    'Ποιά είναι η γλώσσα που μιλιέται σε περισσότερες χώρες;': 'Αγγλικά',
    'Ποιά είναι η πρωτεύουσα της Γαλλίας;': 'Παρίσι',
    'Ποιός ανακάλυψε την Αμερική;': 'Κολόμβος'
}


correct_count = wrong_count = 0
#Pick 5 questions 
for erwtiseis in range(5):
    #Random proposal of questions from the sample
    TrapezaErwtisewn=random.choice(list(erwtiseis_Dict.keys()))
    #Show the random questions and take the answer's input
    #Except numbers in quiz answers
    try:
        answer=str(input(TrapezaErwtisewn)) 
        if answer.isdigit() == True:
            raise Exception("Οι σωστές απαντήσεις περιλαμβάνουν μόνο λέξεις")
    except Exception as OnlyAlphas:
        print(f"Error: {OnlyAlphas}")
       
    #Strip the white chars and check if the answer is in dict values
    if answer.strip() in erwtiseis_Dict.values():
        #Show the result in the user
        print("Σωστή απάντηση")
        correct_count+=1
    else: 
        print("Λάθος απάντηση") 
        wrong_count+=1

#Score's percentage
if erwtiseis>0:
    pososto_correct_count=(correct_count/(erwtiseis+1))*100 
    pososto_wrong_count=(wrong_count/(erwtiseis+1))*100
    print(f'Σωστές απαντημένες ερωτήσεις: {correct_count}/5 με ποσοστό επιτυχίας {pososto_correct_count:.1f}%. \nΛάθος απαντημένες ερωτήσεις: {wrong_count}/5 με ποσοστό αποτυχίας {pososto_wrong_count:.1f}%')
else:
    print("Το quiz δεν πραγματοποιήθηκε")
    






