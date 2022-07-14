#a가 b보다 작은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.

a,b = input().split()
if int(a) < int(b):
    print('True')
else:
    print('False')