n = int(input())
overlay = []
for _ in range(n):
    s = input()
    overlay = []
    for i in range(len(s)):
        a = list(s)
        for j in range(len(a) - 1):
            if len(a) == 1: break
            one = a[j]
            two = a[j + 1]
            if one not in overlay and two not in overlay:
                if one != two:
                    overlay.append(one)
            else:
                n -= 1
                break
        break
print(n)
