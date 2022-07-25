# https://www.acmicpc.net/problem/2908

a,b = input().split()

if int(a[3::-1]) < int(b[3::-1]):
    print(b[3::-1])
else:
    print(a[3::-1])