N =  int(input())
result = []
N_list = list(map(int,str(N)))
result.append(N_list[1])
result.append(sum(N_list))
print(result)
