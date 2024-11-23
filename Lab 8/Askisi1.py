'''Γράψτε ένα πρόγραμμα, στο οποίο θα ορίσετε την κλάση Book με χαρακτηριστικά title(τίτλος), author (συγγραφέας),
numpages(αριθμός σελίδων) και year(έτος πρώτης έκδοσης). Η ειδική μέθοδος __str__() θα επιστρέφει τα πλήρη στοιχεία
ενός βιβλίου κατάλληλα μορφοποιημένα. Να ορίσετε, επίσης, τις κατάλληλες μεθόδους getter που θα περιστρέφουν
την τιμή του αντίστοιχου πεδίου. Στο κυρίως πρόγραμμα να δημιουργήσετε 3 στιγμιότυπα της κλάσης και να τα
αποθηκεύσετε σε μία λίστα. Στη συνέχεια εμφανίστε τον μέσο όρο των σελίδων όλων των βιβλίων καθώς και τα πλήρη
στοιχεία του βιβλίου που εκδόθηκε πρώτο από όλα.
'''

class Book:
    def __init__(self,title,author,numpages,year):
        self.title = title
        self.author = author
        self.numpages = numpages
        self.year = year
    
    def gettitle(self):
        return self.title
    def getauthor(self):
        return self.author
    def getnumpages(self):
        return self.numpages
    def getyear(self):
        return self.year
    def __str__(self):
        return f"{self.title} by {self.author}, {self.numpages} pages, published in {self.year}"



if __name__=='__main__':

    stigmiotipo1 = Book('Εισαγωγή στην επιστήμη υπολογιστών','Fourouzan',700,2015)
    #print(stigmiotipo1.gettitle(),stigmiotipo1.getauthor(),stigmiotipo1.getnumpages(),stigmiotipo1.getyear())
    
    stigmiotipo2= Book('Τρεις ευκαιριες','Τατιανα Τζινιωλη',300,2018)
    #print(stigmiotipo2.gettitle(),stigmiotipo2.getauthor(),stigmiotipo2.getnumpages(),stigmiotipo2.getyear())

    stigmiotipo3= Book('Αρχίζει με εμας','Coolean Hoover',150,2024)
    #print(stigmiotipo3.gettitle(),stigmiotipo3.getauthor(),stigmiotipo3.getnumpages(),stigmiotipo3.getyear())
    print(f"{stigmiotipo1} \n {stigmiotipo2} \n {stigmiotipo3}")
    list=[stigmiotipo1,stigmiotipo2,stigmiotipo3]

    first_book = min(list, key=lambda x: x.getyear())
    print(f"Το βιβλιο που εκδόθηκε πρώτο απο όλα είναι το: {first_book}")

    total_pages = sum(book.getnumpages() for book in list)
    average_pages = total_pages / len(list)
    print(f"Ο μέσος όρος των σελίδων όλων των βιβλίων είναι: {average_pages:.2f}")