''''
Let’s assume you posted a story in social media which goes viral today. However haters tries to
troll the content and attacking your comment section! As to neutralize the threat in the comment
section, one way of dealing this situation is to remove all of the vowels from the trolls’ comments.
Design a python code that takes a string argument and returns a new string with all vowels
removed.
'''

v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
k = []
l = ''
x = str(input())
x = list(x)
for j in x:
    if j in v:
        pass
    else:
        k.append(j)
        l=l+j
print(l)