a = 'Eat Work Play Sleep repeat'    # 다음 문자열을 'working playing'으로

w = a[4:8]
p = a[9:13]
i = 'ing'
print(w,p)
W = w.lower(); P = p.lower()
print(W+i,P+i)

    #or
QEQWEQ
A = a.lower()
work = A.find('work')
play = A.find('sleep')
print(A[work:play].replace(' ','ing '))