# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고,
# r1, r2는 10,000보다 작거나 같은 음이 아닌 정수이다.

# 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
a= '''3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5'''
print(a)
try_ = int(a[0])
b = a.split("\n")
print(b)
print(b[1])
for i in range(try_):
    print(i)
    case = b[i+1]
    c = case.split()
    c_int = list(map(int,c))

    r1 = c_int[2];
    r2 = c_int[5]
    x1 = c_int[0]; y1 = c_int[1]
    x2 = c_int[3]; y2 = c_int[4]
    r3 = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    if r1 + r2 < r3:
        print(0,'경우의수')
    elif r1 + r2 == r3:
        print(1,'경우의수')
    elif r3 == 0 and r1 == r2:
        print(-1,'경우의수')
    elif r3 == 0 and r1 != r2:
        print(0,'경우의수')
    elif r1 + r2 > r3:
        print(2,'경우의수')