ans = ''
for i in range(1,int(input())+1):
    N = list(input())
    N.reverse() # N 리스트를 뒤집는다.
    for j in range(len(N)): 
        if N[j] == 'b': # 리스트에 b가 있으면 d로 바꾼다
            N[j] = 'd'
        elif N[j] == 'd': # 리스트에 d가 있으면 b로 바꾼다
            N[j] = 'b'           
        elif N[j] == 'p': # 리스트에 p가 있으면 q로 바꾼다
            N[j] = 'q'          
        elif N[j] == 'q': # 리스트에 q가 있으면 p로 바꾼다
            N[j] = 'p'
    res=''.join(N) #결과값 출력
    print('#{} {}'.format(i,res)) 