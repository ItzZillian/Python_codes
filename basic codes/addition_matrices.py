#Addition of two matrices
a=[]
for i in range(0,3):
    v1=[]
    for j in range(0,3):
        Num=int(input('Numbers:'))
        v1.append(Num)
    a.append(v1)
    
b=[]
for i in range(0,3):
    v2=[]
    for j in range(0,3):
        Num2=int(input('Numbers2:'))
        v2.append(Num2)
    b.append(v2)
    
for i in range(0,3):
    for j in range(0,3):
        print(a[i][j]+b[i][j], end='\t')
    print()


            
