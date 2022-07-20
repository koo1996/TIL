N = list(input()) 

for test in N: #반복문 
    print(ord(test)-64, end=' ') 
    #A는 아스키코드 65 , 65 - 64 부터 
    #하나씩 증가하는 값들을 출력하면 된다.