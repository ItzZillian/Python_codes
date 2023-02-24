#Take 2 strings from the user, replace all A with a, concatenate the strings and print
n = input('Enter string 1:')
m = input('Enter string 2:')
l1 = []
for i in n:
    if i == 'A':
        l1.append(i.lower())
    else:
        l1.append(i)
for i in m:
    if i == 'A':
        l1.append(i.lower())
    else:
        l1.append(i)
print(''.join(l1))