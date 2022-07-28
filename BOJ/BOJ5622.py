alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
N = input()
result = 0
for i in range(len(N)): #입력값 길이만큼 반복
    for j in alphabet:  
        if N[i] in j: #입력값이 alphabet에 포함되면 index에 +3을 해서 출력한다.
            result += alphabet.index(j)+3
print(result)