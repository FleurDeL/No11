def facto(a):
    i = a
    while i > 1:
        a = a*(i-1)
        i -= 1
    return a
t = int(input())
if t == 0: print(0); quit()
T = facto(t)
b = list(str(T))
i = -1
count = 0
while b[i] == '0':
    count += 1
    i -= 1

print(count)