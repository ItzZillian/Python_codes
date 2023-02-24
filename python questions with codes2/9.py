'''
Get a DOB from the user which is an 8 digit number. Check whether it is a Lucky number
or not by following the steps below:
7
Step-1: Calculate the sum of the digits in the odd-numbered positions (the first, third, fifth and
seventh digits) and multiply this sum by 3.
Step-2: Calculate the sum of the digits in the even-numbered positions (the second, fourth,
sixth and eighth digits) and add this to the previous result (got in step 1).
Given Date of Birth is declared as a lucky number, only if the last digit of the result from step
2 is 0.
Develop an algorithm and write a python program to read the Date of Birth, if the number of
digits is not 8 then print “Cannot be processed” and terminate program. If the number of digits
is 8 and if the DOB is a lucky number, output the DOB with the message “Lucky Number.” If
the number of digits is 8 and if the DOB is not a lucky number, output the DOB with the
message “Not a Lucky Number.”
'''

n=input()
sum1=0
sum2=0
if len(n)!=8:
    print('Invalid Input')
else:
    b=n[::2]
    c=n[1::2]
    for i in b:
        sum1 = int(i)+sum1
    for i in c:
        sum2 = int(i)+sum2
        final_sum = 3*sum1 + sum2
    if final_sum%10==0:
        print(n+', Lucky Number')
    else:
        print(n,', Not a Lucky Number')