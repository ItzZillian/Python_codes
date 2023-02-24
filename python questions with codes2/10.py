'''
Given a number ‘n’, write PAC, Algorithm, Flowchart and Python program to print the
digits of ‘n’ that divides ‘n’. Print the digits in reverse order of their appearance in the
number ‘n’. For example, if n is 122 then print 2, 2, 1. Use only conditional and
iterative statements to write the code. If none of the digits divide the number, then print
‘No factors’
'''
n=input()
l1=[]
for i in n:
    if int(n)%int(i)==0:
        l1.append(i)
l1=l1[::-1]
print(' '.join(l1))