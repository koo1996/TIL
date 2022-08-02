N, M = map(int,input().split())

A = set(map(int,input().split())) #A집합 set 생성
B = set(map(int,input().split())) #B집합 set 생성

print(len(A-B) + len(B-A)) # A-B 길이 + B-A 길이