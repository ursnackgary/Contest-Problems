t = int(input())


for _ in range(t):
  n = int(input())
  if n < 1000:
    print('Newbie')

  elif 1000<= n <= 1199:
    print('Amateur')

  elif 1200<= n <= 1499:
    print('Expert')

  elif 1500<= n <= 1799:
    print('Candidate Master')

  elif 1800<= n <= 2199:
    print('Master')

  elif 2200<= n <= 2999:
    print('Grandmaster')

  elif 3000<= n <= 3999:
    print('Target')

  elif 4000<= n :
    print('Rainbow Master')
