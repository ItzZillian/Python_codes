#matrix multiplication
a=[]
for i in range(0,3):
    v1=[int(input('Numbers1:')) for j in range(0,3)]
    a.append(v1)
    
b=[]
for i in range(0,3):
    v2=[int(input('Numbers2:')) for j in range(0,3)]
    b.append(v2)

c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    v3=[]
    for j in range(0,3):
        for k in range(0,3):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
            n3=c[i][j]
            v3.append(n3)
        c.append(v3)
print('Multiplication is:')
for i in range(0,3):
    for j in range(0,3):
        print(c[i][j], end='\t')
    print()


            
