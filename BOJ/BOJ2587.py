list_ = []
for i in range(5):
    N = int(input())
    list_.append(N)

average = sum(list_) / 5
print(int(average))
list_.sort(reverse=True)
print(list_[2])