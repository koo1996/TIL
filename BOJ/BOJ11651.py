import sys
input = sys.stdin.readline

N = int(input())

array = []
for i in range(N):
    x,y = map(int,input().split())
    array.append([y,x])

F_array = sorted(array)

for y, x in F_array:
    print(x,y)