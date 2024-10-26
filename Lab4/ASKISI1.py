
LS_1=[['Alex','Brown'],['John','Toric'],['Maria','Abel'],['George','Stu']]
LS_2=[['Maria','Abel'],['Alexandra','Greg'],['Stannis','Snow']]
Common_LS=[]
print(LS_1[0][0],len(LS_1))
k=y=i=0

while i<=len(LS_1):
    if LS_1[i][y]==LS_2[i][y] :
        if y>i: i+=1
        elif y==1: y=0 
        else: y+=1
        print(i,y,k,LS_1[i][y],LS_2[i][y])
        Common_LS.insert(k,LS_1[i][y]) 
        print(Common_LS)
        k+=1
    else: 
        print(i,y,k,LS_1[i][y],LS_2[i][y])
        if y>i: i=i+1
        elif y==1: y=0 
        else: y+=1
        k+=1
        print("Δεν υπαρχει καποιος κοινος φιλος")
