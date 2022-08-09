N = int(input())

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
for i in range(N):
    X,Y = map(int,input().split())
    if X > 0 and Y > 0:
        Q1 += 1
    elif X < 0 and Y > 0:
        Q2 += 1
    elif X < 0 and Y < 0:
        Q3 += 1
    elif X > 0 and Y < 0:
        Q4 += 1
    else:
        AXIS += 1
print(f'Q1: {Q1}\nQ2: {Q2}\nQ3: {Q3}\nQ4: {Q4}\nAXIS: {AXIS}')