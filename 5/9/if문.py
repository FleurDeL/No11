sentence = 'averythinz' #input('영어 문자열 입력')
a = sentence.count('a')
e = sentence.count('e')
i = sentence.count('i')
o = sentence.count('o')
u = sentence.count('u')
if a+e+i+o+u >= 1:
    print('모음이 들어 있습니다')
else:
    print('모음이 없습니다')
if sentence[-1] == 'z' and sentence[0] == 'a':
    print('알바벳 순 입니다.')
