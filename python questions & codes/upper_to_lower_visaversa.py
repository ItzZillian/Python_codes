#Write a program to print lower when you have upper case letter in string and vice versa.
n = input('Enter the string here:')
l1 = []
for i in n:
    if i>='a' and i<='z':
        l1.append(i.upper())
    elif i>='A' and i<='Z':
        l1.append(i.lower())
    else:
        l1.append(i)
print(''.join(l1))