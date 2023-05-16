T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    r3 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    if r1 < 0 or r2 < 0:
        print('거리 음수')
        exit()
    length = [r1, r2, r3]
    max_ = max(length)
    min_ = min(length)
    del length[length.index(max_)]
    del length[length.index(min_)]
    another = length[0]

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif max_ > min_ + another:
        print(0)
    elif max_ < min_ + another:
        print(2)
    elif max_ == min_ + another:
        print(1)
