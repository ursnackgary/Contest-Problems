a = int(input())
c = int(input())
b = int(input())
d = int(input())

c1 = 0
c2 = 0
c3 = 0
c4 = 0

if a == 1:
  c1 = 461
elif a == 2:
  c1 = 431
elif a == 3:
  c1 = 420
else :
  c1 = 0


if b == 1:
  c2 = 130
elif b == 2:
  c2 = 160
elif b == 3:
  c2 = 118
else :
  c2 = 0

if c == 1:
  c3 = 100
elif c == 2:
  c3 = 57
elif c == 3:
  c3 = 70
else :
  c3 = 0

if d == 1:
  c4 = 167
elif d == 2:
  c4 = 266
elif d == 3:
  c4 = 75
else :
  c4 = 0
sum1 = c1 + c2 + c3+ c4
print("Your total Calorie count is " + str(sum1)+ ".")
