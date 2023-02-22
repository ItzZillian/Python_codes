#biggest and second biggest numbers
x=int(input('Total numbers:'))
a=[]
i=0
while (i<x):
    n=int(input('Enter the number:'))
    a.append(n)
    i+=1
print(a)
big=a[0]
i=0
while (i<x):
    if (a[i]>big):
        big=a[i]
    i+=1
print('biggest is:',big)
smaller=0
i=0
while(i<x):
    if (a[i]>smaller and a[i]<big):
        smaller=a[i]
    i+=1
print('second biggest:',smaller)
    
