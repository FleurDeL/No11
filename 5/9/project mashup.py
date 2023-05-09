#사용자에게 두 개의 성명을 받아 두 이름과 두 성을 조합한 새로운 이름 두개를 만든다.
name1 = input('첫번째 이름')
name2 = input('두번째 이름')

space = name1.find(' ')
name1_first = name1[0:space]
name1_last =  name1[space+1:]
space = name2.find(' ')
name2_first = name2[0:space]
name2_last = name2[space+1:]

print(name1_first, name1_last, name2_first, name2_last)

name1_len = len(name1_first)
name1_len_front = len(name1_first)//2
name1_len_back = name1_len - name1_len_front
name1_llen = len(name1_last)
name1_llen_front = len(name1_last)//2
name1_llen_back = name1_llen - name1_llen_front

name2_len = len(name2_first)
name2_len_front = len(name2_first)//2
name2_len_back = name2_len - name2_len_front
name2_llen = len(name2_last)
name2_llen_front = len(name2_last)//2
name2_llen_back = name2_llen - name2_llen_front

print(
    name1_first[0:name1_len_front]+name2_first[name2_len_front:],
    name2_first[0:name2_len_front]+name1_first[name1_len_front:],

    name1_last[0:name1_llen_front] + name2_last[name2_llen_front:],
    name2_last[0:name2_llen_front] + name1_last[name1_llen_front:]
);