str1 = input()
hcount = 0
vcount = 0

for char in str1:
  if char == 'H':
    hcount += 1
    
  if char == 'V':
    vcount += 1

if hcount % 2 == 0:
  if vcount % 2 == 0:
    print(1,2)
    print(3,4)
  else:
    print(2,1)
    print(4,3)

else:
    if vcount % 2 == 0:
        print(3,4)
        print(1,2)
    else:
        print(4,3)
        print(2,1)
        
