#Write a program to print a list of odd numbers from the list of numbers given by the user using list comprehension.
n = [int(num) for num in eval(input("Enter list of numbers:"))]
odd_n = [num for num in n if num % 2 != 0]
print("Odd numbers:", odd_n)
