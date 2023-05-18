def fibonacci(n):
    if n == 0:
        print("0")
        return 0
    elif n == 1:
        print("1")
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = list(map(int, input().split()))
a = 1
factor = []
for i in range(min(T)):
    if max(T) % a == 0 and min(T) % a == 0:
        factor.append(a)
    a += 1
print(max(factor))

l = 1
list_i = []
for i in range(min(T)):
    if (max(T)*l) % min(T) == 0:
        print(max(T)*l)
        break
    else: l += 1
