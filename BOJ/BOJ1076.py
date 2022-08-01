Color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
Numbers = [0,1,2,3,4,5,6,7,8,9]
Numbers_2 = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

A = input()
B = input()
C = input()
for i in Color:
    if A == i:
        X = Color.index(i)
for j in Color:
    if B == j:
        Y = Color.index(j)
        Y_ = Numbers[Y]
for u in Color:
    if C == u:
        Z = Color.index(u)
        Z_ = Numbers_2[Z]
# print(X * Y_ * Z_)
print((X * 10 + Y) * Z_)

