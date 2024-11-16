import csv 
filename='tasks.csv'

def typwsi_plithos(filename):
    sum=0
    with open(filename,'r',encoding='utf-8') as f:
        for row in f:
            for cell in row:
                if cell.strip():
                    sum+=1
    return print(sum)
        
typwsi_plithos(filename)