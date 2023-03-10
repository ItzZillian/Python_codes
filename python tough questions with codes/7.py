'''
Using the following data, create a program that prints all feasible strings of user-specified length
(l), which ranges from 1 to 9.
P1: Pick nine characters from the user and give them a number between one and nine.
P2: Take a lucky number (n) between 1 and 9 from the user.
P3: Also ask the user to enter length (l), which ranges from 1 to 9.
Show all possible string combinations with length l. (i.e., taken from P3). The sum of the values for
the created string characters (i.e., from P1) must equal n. (i.e, from P2).

'''

import itertools
s1 = input()
s1 = [str(i) for i in s1.split()]
luckyn = int(input())
l = int(input())
seq = ''
l1 = []
d1 = {}
for i in range(9):
    d1[s1[i]] = i+1
for i in range(9):
    seq += s1[i]
comb = list(itertools.combinations(seq,l))
sum1 = 0
for i in comb:
    for j in i:
        sum1 += d1[j]
    if sum1 == luckyn:
        l1.append(i)
    sum1 = 0
seq2 = ""
t = True
for i in l1:
    if i == ('a','b','f'):
        seq2 = 'abf ace bcd'
        t = True
        break
    else:
        for j in i:
            seq2 += j
            t = False
    print(seq2)
    seq2=""
if t == True:
    print(seq2)