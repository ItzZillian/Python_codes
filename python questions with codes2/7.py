'''Write a PAC chart, flowchart, algorithm and python code for the question given below.
An online educational platform offers three courses: Programming Courses, Robotics
Courses and Academic Writing Courses : The vendor gives a discount of 10% on orders
for programming based courses if the order is for more than Rs. 1000. On orders of more
than Rs. 750 for Robotics Courses, a discount of 5% is given, and a discount of 10% is
given on orders for academic writing courses of value more than Rs. 500. Assume that the
numeric codes 1,2 and 3 are used for Programming, Robotics and Academic Writing
Courses respectively. Write a program that reads the product code and the order amount
and prints out the net amount that the learner is required to pay after the discount.'''

n=int(input())
m=int(input())
if n==1:
  if m>1000:
   print(format(m-m*0.1,'.2f'))
 else:
  print(format(m,'.2f'))
if n==2:
 if m>750:
  print(format(m-m*0.05,'.2f'))
 else:
  print(format(m,'.2f'))
if n==3:
 if m>500:
  print(format(m-m*0.1,'.2f'))
 else:
  print(format(m,'.2f'))