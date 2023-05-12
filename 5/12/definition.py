def get_word(word1, word2):
    word = word1 + word2
    return len(word)
print(get_word('2', '3'))

def func_1(sign):
    return len(sign)        #반환값 : sign의 길이, 타입은 int

def func_2():
    return (True and True)  #반환값 : True, 타입은 bool

def func_3(머리, 어깨, 무릎):
    return ('발')            #반환값 : '발' 타입 str

def add_sub(n1, n2):
    add = n1 + n2
    sub = n1 - n2
    return (add, sub)
print(add_sub(3, 4))
머리 = 1; 어깨 = 2; 무릎 =3
print(func_3(머리,어깨,무릎))
