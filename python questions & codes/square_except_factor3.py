#Write a program to print the squares of all numbers except for factors of 3.
n = int(input('Enter the Number:'))
for i in range(1,n+1):
    if i%3!=0:
        print(i**2)