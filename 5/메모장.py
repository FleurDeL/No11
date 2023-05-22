def d(i):
    if i < 10:
        return i*2
    elif 10 <= i and i < 100:
        return i + i//10 + i%10
    elif 100 <= i and i < 1000:
        return i + i//100 + (i%100)//10 + (i%100)%10
    elif 1000 <= i and i < 10000:
        return i + i//1000 + (i%1000)//100 + (i%1000)%100//10 + ((i%1000)%100)%10  #1221
T = [i for i in range(1,10001)]

for i in range(1,100):
    while i < 10000:
        if d(i) in T:
            T.remove(d(i))
        i = d(i)
for i in range(len(T)): print(T[i])