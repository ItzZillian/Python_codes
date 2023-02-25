'''
Create a Python code that takes every object from the list and check if it has list object or not. If a
list object is present in a list, it should be unpacked and the overall count of the list should be
conveyed. If list object is not present in the existing list, it should say “cannot unpack”
'''
n = eval(input())
a = len(n)-1
num = False
for i in n:
    if type(i) == list:
        num = True
    for j in i:
        a+=1
if num == False:
    print('Cannot Unpack')
else:
    print(a)