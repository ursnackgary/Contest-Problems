limit = int(input())
speed = int(input())

if speed > limit:
  ex = speed - limit
  if 1 <= ex <= 20:
    print("You are speeding and your fine is $100.")
  elif 21 <= ex <= 30:
    print("You are speeding and your fine is $270.")
  elif 31 <= ex :
    print("You are speeding and your fine is $500.")
else: 
  print("Congratulations, you are within the speed limit!")
