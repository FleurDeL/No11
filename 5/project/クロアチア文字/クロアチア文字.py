a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
T = 'ddz=z='

j = 0
for i in range(len(T)):
    j += 1
    t = T[j-1]+T[j]
    print(t,j)
    if t in a:
        count += 1
        j += 1
    elif t not in a:
        count += 1
    elif t == 'dz' and T[j+1] == '=':
        count += 1
        j += 2
        print('yeah')
    print(count)
    if j >= len(T)-1: break
'''if T[-2]+T[-1] not in a:
    count += 1
    print('aa')'''
print(count)