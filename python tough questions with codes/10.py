'''
Assume you input a lower case string. Find the length of the longest substring of given string such
that the characters in it can be rearranged to form a palindrome.
'''

import re
x=input()
if len(re.findall('[a-z]',x))==len(x):
    l=[]
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i:j]==x[j:i:-1]:
                l.append(j-i+1)
    print(max(l))
else:
    print('Invalid Input')