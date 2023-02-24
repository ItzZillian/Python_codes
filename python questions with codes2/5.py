'''Write a PAC chart, flowchart, algorithm and python code.
Calculate the toll charge, by considering kilometers travelled by vehicle. Display the toll charge
of the two-wheeler to be paid as per chart below.
kilometers travelled        Charge
KmTr <=1000KM               0
1000KM< KmTr <= 10000       50
1000KM < KmTr <= 20000      150
2000KM < KmTr <= 40000      250
4000KM < KmTr <= 60000      350
KmTr > 60000                500
'''

n=int(input())
if n<=1000:
 print(0)
elif n>1000 and n<=10000:
 print(50)
elif n>10000 and n<=20000:
 print(150)
elif n>20000 and n<=40000:
 print(250)
elif n>40000 and n<=60000:
 print(350)
else:
 print(500)