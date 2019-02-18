best1 = (0 ,"")
best2 = (0, "")

def better(current, prev):
    return (current[0] > prev[0]) or \
    (current[0] == prev[0] and current[1] < prev[1])

N = int(input())

for _ in range(N):
    line = input()
    name = line.split()[0]
    R = int(line.split()[1])
    S = int(line.split()[2])
    D = int(line.split()[3])
    score = 2*R+3*S+D
    current = (score, name)

    if better(current, best1):
        best2 = best1
        best1 = current
        

    elif better(current, best2):
        best2 = current
        
if N> 1:
  print(best1[1])
  print(best2[1])

elif N == 1:
  print(best1[1])
