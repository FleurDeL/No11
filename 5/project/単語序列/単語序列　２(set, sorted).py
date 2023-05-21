n = int(input())


arr = set()
for _ in range(n):
    s = input()
    print(s)
    arr.add(s)

arr = list(arr)

arr = sorted(arr, key = lambda x :len(x))

'''for v in arr:
    print(v)'''