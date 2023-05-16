import re
def find_concatenated_numbers(string):
    pattern = r'\d{2,}'
    numbers = re.findall(pattern, string)
    return numbers

a = '([()][[]])([()]([])(()))'

if '()' in a:
    a = a.replace('()', '2')
if '[]' in a:
    a = a.replace('[]','3')
print(a)
##########################


for i in range(2,4):
    a = a.replace('[%d]'%i,str(i*3))
    i += 1
for i in range(2,4):
    a = a.replace('(%d)'%i,str(i*2))
    i += 1
b = find_concatenated_numbers(a)
print(a)
print(b)
print(len(b[0]))

'''i = 0; j = 0
for i in range(len(b)):
    sum_ = 0
    for j in range(len(b[i])):
        print('길이는', len(b[i]))
        print('j는', j)
        print('b[%d][%d]는'%(i,j),b[i][j])
        sum_ += int(b[i][j])
        j += 1
    b[i] = str(sum_)
    print(sum_)
    i += 1
for i in range
print(b)


'''