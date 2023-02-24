'''A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user such as Number of classes held, Number of classes
attended and also student medical proof availability [1(for Yes)/0 (for No)]. Display
percentage of class attended and eligibility detail (Allowed/ Not Allowed) for exam. If
student is having less than 75% but having medical proof, he/she is ‘Allowed’ for exam,
otherwise "Not Allowed" '''
n=int(input())
m=int(input())
o=int(input())
p=(m/n)*100
if p>75:
 print(int(p))
 print('Allowed')
elif p<75 and o==1:
 print(int(p))
 print('Allowed')
else:
 print(int(p))
 print('Not allowed')