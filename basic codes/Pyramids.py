"""
3rd pyramid
n=int(input('Enter Number of lines'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i )
"""
"""
4th pyramid
n=int(input('Enter Number of lines'))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(1,n):
    print(' '*(i)+'*'*(2*(n-i)-1))
"""
"""
5th pyramid

n=int(input('Enter Number of lines'))
print(' '*(n-1)+'*')
for i in range(1,n):
    print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*')
for i in range(1,n):
    print(' '*(i-1)+'*'+' '*(2*(n-i)-1)+'*')
print(' '*(n-1)+'*')
"""   
