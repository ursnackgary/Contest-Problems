a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())

a1 = a1*3
b1 = b1*3
a2 = a2*2
b2 = b2*2

if a1 + a2 + a3 > b1 + b2 + b3:
  print('A')

elif a1 + a2 + a3 < b1 + b2 + b3:
  print('B')

else: 
  print('T')
