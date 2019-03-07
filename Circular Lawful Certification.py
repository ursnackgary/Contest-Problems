da = int(input())
ev = int(input())
w = int(input())

sum1 = 0
if da - 100 > 0:
  sum1 = (da-100)*0.25 + ev*0.15 + w*0.2
else:
  sum1 = ev*0.15 + w*0.2

sum2 = 0

if da - 250 > 0:
  sum2 = (da-250)*0.45 + ev*0.35 + w*0.25
else:
  sum2 = ev*0.35 + w*0.25

sum1 = round(sum1, 2)
sum2 = round(sum2, 2)

print ("Plan A costs " + str(sum1))
print ("Plan B costs " + str(sum2))



str1 = "Plan A is cheapest."
str2 = "Plan B is cheapest."
if sum1 > sum2:
  print(str2)

if sum1 < sum2:
  print(str1)

if sum1 == sum2:
  print("Plan A and B are the same price.")
