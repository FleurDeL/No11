num = int(input('finding index of 1:'))

b = 0
bin_num = bin(num)[::-1]    # [::-1]로 이진법 만들자마자 역순으로 만들기
for i in range(len(bin_num[:-2])):  # 뒤에 붙는 0b는 제외
    if bin_num[b] == '1':
        print(b, end=' ')
    b += 1

