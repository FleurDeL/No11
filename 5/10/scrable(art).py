word_string = '''art
hue
ink
bank
'''

tiles = "hikalauune"

start = 0; end = 0                              #단어의 인덱스 찾을 처음과 끝 변수
word = ()                                       #단어 포함시킬 튜플
found_word = ()                                 #타일로 만들 수 있는 단어 (찾은 단어)
for letter in word_string:                      #입력받은 문자열 스캔
    if letter == '\n':                          #새줄문자 감지되면 그 전까지는 한단어
        word_found = word_string[start:end]     #찾은 문자는 문자열의 인덱스로 지정
        print(word_found)
        w = (word_found,)
        word += w                               #word = word + (word_string[start:end],) 축약가능
        end += 1                                #새줄문자 바로 다음 문자로 리셋 (다른 단어 찾기 시작)
        start = end                             #처음처럼 모든 변수 리셋
    else:
        end += 1                                #end하나씩 늘려가며 문자 길이 늘리기
print(word)
print(word[0])
print('----')
for words in word:                              #words 는 word에 있는 문자들
    tiles_left = tiles                          #문자들의 단어가 타일 안에 있으면 그 타일을 뺸다
    for letter in words:                         #문자들은 하나씩 스캔
        if letter not in tiles_left:            #스캔한 문자가 타일에 없으면 루프 나옴
            break
        else:                                   #타일에 있으면
            index = tiles_left.find(letter)     #그 문자의 인덱스 추출해서
            tiles_left = tiles_left[:index]+tiles_left[index+1:]    #그 인덱스를 뺸 나머지가 남은 타일들
    if len(words) == len(tiles)-len(tiles_left): #제거한 타일의 개수가 단어의 길이랑 같으면 찾은 문자로
        found_word = found_word + (words,)
print(found_word)

# if Is_in_tiles == -1:
 #       print('불가능')
#       Is_in_tiles = tiles.find(letter_of_words)
#       break                                     #만약 없으면 불가능 출력하고 if 문 나오기
#    else:
#        print('그다음문자')
 #       a += 1
##        Is_in_tiles = tiles.find(letter_of_words) #있으면 그 다음문자로 넘어가서 또 찾기
#                           #다 끝났으면 그 다음 단어로 넘어가기'