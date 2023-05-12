def sandwich(kind_of_sandwich):     #여기서는 매개변수
    print('----------')
    print(kind_of_sandwich())       #여기서는 뒤에 괄호 붙임으로써 함수 호출임을 표현
    print('----------')

def blt():
    my_blt = ' 베이컨\n 상추\n 토마토'
    return my_blt
def breakfast():
    my_ec = ' 달걀\n 치즈'
    return my_ec

print(sandwich(blt))