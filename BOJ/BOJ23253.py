A,B = map(int,input().split())

M = int(input())
list_1 = list(map(int,input().split()))
print(list_1)

N = int(input())
list_2 = list(map(int,input().split()))
print(list_2)

stack = []

for i in range(max(len(list_1,list_2))):
    if list_1[M-1] < list_1[N-1]:
        list_1.pop()
        list_2.pop()


# for i in range(A):
#     if list_1[-1] < list_2[-1]:
#         list_1.pop()
#         result.append(list_1.pop)
#         list_2.pop()
#         result.append(list_2.pop)
#     else:
#         list_2.pop()
#         result.append(list_2.pop)
#         list_1.pop()
#         result.append(list_1.pop)

# print(result)