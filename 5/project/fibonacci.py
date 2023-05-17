# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
def fibonacci(n):
    global num_0
    global num_1
    if n == 0:
        num_0 += 1
        return 0
    elif n == 1:
        num_1 += 1
        return 1
    else:
        b.append(n)
        return fibonacci(n - 1) + fibonacci(n - 2)

num_0 = 0
num_1 = 0
b = []
print(fibonacci(30))

'''T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    if fibonacci(a[0]) in b:
        print(fibonacci(a[0]))
        exit()
    fibonacci(a[0])
    print(num_0,num_1)
'''