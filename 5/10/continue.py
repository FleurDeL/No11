x = 0
for x in range(100):
    print('x는',x)
    if x <= 5:
        continue
    print('x가 5보다 큽니다')
    if x%10 == 0:
        continue
    print('x를 10으로 나눌 수 없습니다')
    if x!=2 and x!=4 and x!=16 and x!=32 and x!=64:
        continue
    print('x는 2의 거듭제곱 수입니다')
    