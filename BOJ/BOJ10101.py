A = int(input())
B = int(input())
C = int(input())

if A + B + C == 180:
    if A == B == C == 60:
        print('Equilateral')
    elif A == B or B == C or A == C:
        print('Isosceles')
    elif A != B != C:
        print('Scalene')
else:
    print('Error')