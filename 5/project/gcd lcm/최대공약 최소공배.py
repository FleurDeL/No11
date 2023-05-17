#입력
#첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

#출력
#첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
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
    list_i.append(max(T)*l)
    l += 1
m = 1
list_j = []
for j in range(max(T)):
    list_j.append(min(T)*m)
    m += 1
list_k = []
for k in range(len(list_i)):
    if list_i[k] in list_j:
        list_k.append(list_i[k])
    k += 1

if len(list_k) == 0:
    print('공배수 없음')
else:
    print(min(list_k))