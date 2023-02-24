'''Write a PAC Chart, algorithm, and flowchart for converting the given two-digit number
into its corresponding Roman numeral'''

n=int(input())
num_map=[(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
roman=''
while n>0:
 for i,r in num_map:
  while n>=i:
   roman+=r
   n-=i
print(roman)