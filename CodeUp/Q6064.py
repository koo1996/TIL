#가장 작은 값을 출력한다.

a,b,c = input().split()

if int(a)<int(b):
    if int(a)<int(c):
        print(a)
    else:
        print(c)
elif int(b)<int(c):
    if int(b)<int(a):
        print(b)
    else:
        print(a)
else:
    print(c)        