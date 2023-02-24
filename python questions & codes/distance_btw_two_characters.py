#Calculate the distance between any two characters given by the user
n = input('Enter letter 1:').lower()
m = input('Enter letter 2:').lower()
a = ord(m)
b = ord(n)
if b>a:
    a , b = b , a
print(a-b)