# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# N！の中で後ろから初めての０ではない数字が出るまでの０の数を出力する。


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