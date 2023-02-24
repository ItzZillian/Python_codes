#Write a function which prints all the numbers divisible by 3 and 5.
n = int(input('Enter number 1 here:'))
m = int(input('Enter number 2 here:'))
if n > m:
    m, n = n, m
for i in range(n, m+1):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)