'''Draw a flowchart and construct a python program to accept the monthly income
of an employee and display the income tax to be paid at the end of the year
according to the following criteria:
Annual income (in Rs)      Income Tax
> 1000000                  4 %
> 500000 and <= 1000000    2 %
<= 500000                  NIL                     '''

n=int(input())
if n>1000000:
 print(int(n*0.04))
elif n>500000 and n<=1000000:
 print(int(n*0.02))
else:
 print('NIL')