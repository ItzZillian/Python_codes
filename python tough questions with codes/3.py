'''
Write a Python code for the following:
• A list has the objects of maximum 2 strings, 2 complex numbers and 2 integers.
• If atleast one integer object is prime, all strings should be reversed and the real part as well as
the imaginary part of all the complex numbers should be interchanged
• if atleast one string object is palindrome, all the complex numbers should be conjugated and the
integer objects should be negated.
• If both of the above conditions are satisfied, print the middle element of the list.
• If none of the above conditions satisfied, convert all the strings into list object.
'''

a=eval(input())
list=[]
c1=False
c2=False
if len(a)==1:
    print('Invalid Data')
else:
    for i in a:
        if type(i)==int:
            for j in range(2,int(i)-1):
                if type(j)==int and i%j==0:
                    c1=False
                    break
                else:
                    c1=True
                    break
    for i in a:
        if type(i)==str:
            i=i.lower()
            if i[::-1]==i:
                c2=True
            if c1==True and c2==True:
                b=int(len(a)/2)
                print(a[b])
            elif c1==False and c2==False:
                for i in a:
                    if type(i)==str:
                        for j in i:
                            list.append(j)
                    else:
                        list.append(i)
                    print(list)
                else:
                    if c1==True:
                        for i in a:
                            if type(i)==str:
                                list.append(i[::-1])
                            elif type(i)==int:
                                list.append(i)
                            elif type(i)==complex:
                                r=i.real
                                im=i.imag
                                i=complex(im,r)
                                list.append(i)
                        print(list)
                    if c2==True:
                        for i in a:
                            if type(i)==str:
                                list.append(i)
                            elif type(i)==int:
                                list.append(-i)
                            elif type(i)==complex:
                                list.append(i.conjugate())
print(list)