n=input()
a=''
for i in n:
    if i<='Z' and i>='A':
        i=i.lower()
        a+=i
    else:
        a+=i
print(a)
    
