#Write a function which returns the number of vowels present in a string.
n = input('Enter your string here:')
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
l1 = []
for i in n:
    if i in vow:
        l1.append(i)
print(l1)
print('Number of vowels in string =',len(l1))