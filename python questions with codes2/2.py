'''Petrol is collected for Indian Oil Corporation for sales from nearest ‘n’ storage
points to the Collection point. Given the amount of petrol from ‘n’ storage points
in litres(L) and milli litres (mL), write a PAC chart, flowchart, algorithm and
python code to compute the total quantity of oil in the collection point.
For example, if oil comes from 3 bunks in quantities 2 L 300 mL, 3 L 700 mL and 4 L
600 mL then the total quantity of oil in collection is 10 L 600 mL.'''

n=int(input())
sum1=0
sum2=0
rem=0
for i in range(0,n):
 m=int(input())
 n=int(input())
 sum1+=m
 sum2+=n
if sum2>=1000:
 rem=sum2//1000
print(sum1+rem, sum2%1000)