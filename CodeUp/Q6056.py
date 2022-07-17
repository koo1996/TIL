#두 값의 True / False 값이 서로 다를 경우만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
a,b = input().split()

if bool(int(a)) != bool(int(b)):
    print('True')
else:
    print('False')