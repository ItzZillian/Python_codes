#Take a list of all elements from the user and find the square root of each number in the list and store it in another list and print that list.
n = eval(input('list of elements:'))
l1 = []
for i in n:
    a = i**(1/2)
    l1.append(a)
print(l1)