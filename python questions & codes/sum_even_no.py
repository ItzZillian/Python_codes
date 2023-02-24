#Write a program to find the sum of all even numbers in a list.
n = eval(input('Enter the list of numbers here:'))
sum1 = 0
for i in n:
    if i%2 == 0:
        sum1+=i
print(sum1)
