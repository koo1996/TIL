N = input()
CR_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for test in CR_list: 
    N = N.replace(test,'@') #N에 CR_list 문자열이 있다면 @로 바꾼다. 
print(len(N))  #바뀐 N의 길이를 구한다.