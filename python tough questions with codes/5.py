'''
Calculate the following numbers in numerology using below table. (using Set only)
'''

n=input()
a=[]
p=0
q=0
r=0
s=0
t=0
e=0
f=0
for i in n:
    a.append(i)

s1={'A','J','S'}
s2={'B','K','T'}
s3={'C','L','U'}
s4={'D','M','V'}
s5={'E','N','W'}
s6={'F','O','X'}
s7={'G','P','Y'}
s8={'H','Q','Z'}
s9={'I','R'}
for i in a:
    if i in s1: p=p+1
    if i in s2: p=p+2
    if i in s3: p=p+3
    if i in s4: p=p+4
    if i in s5: p=p+5
    if i in s6: p=p+6
    if i in s7: p=p+7
    if i in s8: p=p+8
    if i in s9: p=p+9
if p>=10:
    x=p%10
    p=p//10
    q=p+x
else:
    q=p
print(q)
for j in a:
    if j=='A':
    s=s+1
    if j=='E':
    s=s+5
    if j=='I':
    s=s+9
    if j=='O':
    s=s+6
    if j=='U':
    s=s+3
if s>=10:
    x=s%10
    s=s//10
    t=s+x
else:
    t=s
print(t)
s10={'J','S'}
s11={'B','K','T'}
s12={'C','L'}
s13={'D','M','V'}
s14={'N','W'}
s15={'F','X'}
s16={'G','P','Y'}
s17={'H','Q','Z'}
s18={'R'}
for i in a:
    if i in s10: e=e+1
    if i in s11: e=e+2
    if i in s12: e=e+3
    if i in s13: e=e+4
    if i in s14: e=e+5
    if i in s15: e=e+6
    if i in s16: e=e+7
    if i in s17: e=e+8
    if i in s18: e=e+9
if e>=10:
    x=e%10
    e=e//10
    f=e+x
else:
    f=e
print(f)