a = int(input())

for _ in range(int(a)):
    T = list(map(int, input().split()))
    T.sort()
    print(T[-3])