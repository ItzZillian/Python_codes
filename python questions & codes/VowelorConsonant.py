#Write a program to check whether the given letter is a vowel or a consonant.
n = input('Enter your letter here:')
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if n in vow:
    print(n, 'is a vowel')
else:
    print(n, 'is a consonant')
