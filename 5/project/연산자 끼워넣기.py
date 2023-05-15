#a의 첫번째줄에는 숫자의 개수, 두번째 줄에는 그 숫자들을 순서대로 나열, 세번쨰 줄에는 첨부터 덧 뺄 곱 나로
#몇 개씩 있는지 나타냄. 숫자들은 고정된 상태로 사이사이에 기호를 끼워넣어서 연산을 시켜라
#이 때, 연산자는 랜덤으로 끼워 넣는다.
import random
a = '''6
1 2 3 4 5 6
2 1 1 1'''

list_num = []
i_ = 2
for i in range(int(a[0])):
    list_num.append(a[i_])
    i_ += 2
list_num = list(map(int, list_num))
############################# 숫자 리스트 완성
moji_num = []
for i in range(int(a[i_])):
    moji_num.append('+')
i_ += 2
for i in range(int(a[i_])):
    moji_num.append('-')
i_ += 2
for i in range(int(a[i_])):
    moji_num.append('*')
i_ += 2
for i in range(int(a[i_])):
    moji_num.append('%')
############################        문자 리스트 완성
result_list = []
for i in range(100):
    moji_num_ran = random.sample(moji_num, len(moji_num))   # 랜덤 문자리스트 생성
    result = list_num[0]            # 연산 시작
    b = list_num[1]
    def calcul(moji):
        global result
        if moji == '+':
            result += b
        elif moji == '-':
            result -= b
        elif moji == '*':
            result *= b
        elif moji == '%':
            result = (-result//b)*-1
        return result
    result = calcul(moji_num_ran[0])
    j_ = 1
    for i in range(len(moji_num)-1):
        b = list_num[j_+1]
        calcul(moji_num_ran[j_])
        j_ += 1

    if result not in result_list:
        result_list.append(result)

print(max(result_list))
print(min(result_list))