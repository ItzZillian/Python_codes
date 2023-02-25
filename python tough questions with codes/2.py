'''
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users (using tuples only)
'''

n = tuple(input().split(','))
a = True
t = 0
for i in n:
    if len(i) > 12 or len(i) < 6:
        a = False
    for j in i:
        if j >= 'a' and j <= 'z':
            break
        elif j >= 'A' and j <= 'Z':
            break
        elif j == '$' or j == '#' or j == '@':
            break
        elif int(j) >= 0 and int(j) <= 9:
            break
        else:
            a = False
    if a == True:
        print(i)
        t=1
    if t==0:
        print('invalid')