word_string = '''art
hue
ink
'''

start = 0; end = 0                              #단어의 인덱스 찾을 처음과 끝 변수
word = ()                                       #단어 포함시킬 튜플
for letter in word_string:                      #입력받은 문자열 스캔
    if letter == '\n':                          #새줄문자 감지되면 그 전까지는 한단어
        word_found = word_string[start:end]     #찾은 문자는 문자열의 인덱스로 지정
        print(word_found)
        word = word_found
        end += 1                                #새줄문자 바로 다음 문자로 리셋 (다른 단어 찾기 시작)
        start = end                             #처음처럼 모든 변수 리셋
    else:
        end += 1                                #end하나씩 늘려가며 문자 길이 늘리기
print(word)