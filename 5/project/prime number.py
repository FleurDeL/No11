'''1
9'''
a = int(input())

T = list(map(int, input().split()))

for i in range(len(T)):
    k = 2
    if T[i] == 1:
        num -= 1
    else:
        for j in range(T[i] - 2):
            nokori = T[i] % k
            if nokori == 0:
                num -= 1
                break
            k += 1
        i += 1


print(num)