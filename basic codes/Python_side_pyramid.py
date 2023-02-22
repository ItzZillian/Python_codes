a=input('symbol:')
b=int(input('number of lines:'))
for k in range(b):
  for i in range(b):
    for f in range(i):
      print(a , end='')
    print(' ')  
  for i in range(b,0,-1):
    for f in range(i):
      print(a , end='')
    print('')  

