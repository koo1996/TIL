# A,B,C = map(int,input().split())
park_ = []
for _ in range(100):
    park_.append(0)

for _ in range(3):
    x,y = map(int,input().split())
    for i in range(x,y+1):
        park_.append(1)
        print(park_)
