num = int(input('finding index of 1:'))
find_list = []

bin_num = bin(num)[2:]

b = -1  # 오른쪽 끝 개체부터 불러오기

for i in range(len(bin_num)):
    a = bin_num[b]
    if a == '1':
        print(-b - 1, end=' ')  # 객체 인덱스 사용하여 1의 위치 출력
    b -= 1
