N = input()
list_ = []
for i in range(len(N)):
    list_.append(N[i:])
list_.sort()
print(*list_,sep='\n')