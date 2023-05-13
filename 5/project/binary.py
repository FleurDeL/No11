num = int(input('finding index of 1:'))  # 수 입력 받기
find_list = []  # 1이 있는 위치 받는 리스트

bin_num = bin(num)[2:]  # bin은 앞에 0b붙으니 그 다음부터 불러오기
b = 0  # 문자열의 왼쪽부터 불러오기
for i in range(len(bin_num)):  # 이진수 수열 만큼 반복
    pos = -(b - len(bin_num) + 1)  # 인덱스 활용한 연산으로 낮은 위치부터 출력하도록
    a = bin_num[b]
    if a == '1':
        find_list.append(pos)  # 1일때 그 위치 리스트에 추가
    b += 1

find_list.reverse()  # 1의 위치가 감소하는 순서이므로 증가열로 바꿈
for i in range(len(find_list)):
    print(find_list[i], end=' ')  # 숫자랑 빈칸만 나와야하므로 리스트안 객체와 빈칸 출력
