'''Να δημιουργήσετε ένα dataframe 4x5 με τιμές από το 1 έως το 20 και στη συνέχεια να δημιουργήσετε
 με τις κατάλληλες εντολές ένα νέο dataframe, το οποίο θα αποτελείται από τη δεύτερη και τρίτη γραμμή
   του αρχικού.'''

import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(1,20),index=['Γραμμη 1','Γραμμη 2','Γραμμη 3','Γραμμη 4'],columns=['A','B','C','D','E'])
print(df)
data2= df[1:3]
df2 = pd.DataFrame(data2)
print(f"\n\n{df2}")
