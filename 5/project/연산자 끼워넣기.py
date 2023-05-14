import random
a = '''6
1 2 3 4 5 6
1 2 3 0'''
list_num = []
i_ = 2
for i in range(int(a[0])):
    list_num.append(a[i_])
    i_ += 2
print(a[i_])
#############################
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
moji_num_ran = random.sample(moji_num, len(moji_num))
print(list_num, moji_num, moji_num_ran)
list_num = list(map(int, list_num))
result = list_num[0]
b = list_num[1]
def calcul(moji):
    if moji == '+':
        result += b
    elif moji == '-':
        result -= b
    elif moji == '*':
        result *= b
    elif moji == '%':
        result /= b
    return  result
j_ = 1
for i in range(len(moji_num)-1):
    calcul(moji_num_ran[j_])
    j_ += 1