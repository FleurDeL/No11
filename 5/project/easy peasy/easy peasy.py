T = list(map(int, input().split()))
a = [1,1,1]
sum_ = 0
for i in range(1000):
    if a[2] >= T[0]:
        sum_ += a[0]
        if a[2] == T[1]:
            break
    if a[1] == a[0]:
        a[0] += 1
        a[1] = 0
    a[1] += 1
    a[2] += 1
print(sum_)
