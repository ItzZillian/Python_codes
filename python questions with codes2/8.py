'''Earthquake Research Institute of Japan has recorded earthquake occurred in the year 2021
using Richter scale. Develop PAC, Algorithm, Flowchart and write a Python program to
get the ’n’ (number of times) the earthquake has occurred and print the number of times in
which the magnitude was low, medium and high. The magnitude value is given in microns.
If the value is less than 5.4(inclusive) in microns then it is low, 5.4 to 7.0 (inclusive) it is
medium and more than 7.0 it is high.
Also, if the number of times recorded is Zero, display as “No earthquake predicted” and
if the number of times recorded is negative, display as “Invalid Input”
'''
n=int(input())
low=0
medium=0
high=0
if n<0:
    print('Invalid Input')
elif n==0:
    print('No earthquake predicted')
elif n>1:
    for i in range(0,n):
        m=float(input())
    if m<=5.4:
        low+=1
    elif m>5.4 and m<=7.0:
        medium+=1
    else:
        high+=1
print(low)
print(medium)
print(high)