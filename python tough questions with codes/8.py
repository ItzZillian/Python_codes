'''
There is a crime scene (let’s say burglary) happened and the forensic people collected a hair
sample from that scene. Now it is the task of the forensic person to checkout DNA sequence of the
hair sample is matching with the suspected person (say X) or not.
[Hint: The DNA sequences are unique for every individual. That is, one person’s DNA sequence
should not repeat for another person’s DNA. Thus, the uniqueness is identified through the
maximum count of repetition of code “AGCT” subsequence (as shown below).
Person 1: GCCAGCTAGCTAGCTAGCTAGCTAGCTAGCTTTTGGGAGCTAGCTAGCTG…… (7 AGCT
sequences)
Person 2: GCCAGCTAGCTAGCTAGCTTTAGCTAGCTCCGGA……….. (4 AGCT sequences) ]
Write a python code that accepts the hair sample DNA sequence as well as Person X DNA
sequence. If there is exact match of position and maximum count of AGCT sequence, there is a
match; otherwise, it is a mismatch. Also, if the input sequence has anything apart from AGCT and
their combinations, it is a clear mismatch irrespective of count and position
'''

import re
x = input()
y = input()
if len(re.findall('AGCT',x))==len(re.findall('AGCT',y)):
    print('MATCH')

else:
    print('MISMATCH')