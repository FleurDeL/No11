import re

a = '([()][[]])([])'
#b = re.sub()

s = 'Hello, World 2!'
s = re.sub('[^a-z0-9]', '', s)
print(s)

for i in range(2,4):
    a = a.replace('[%d]'%i,str(i*3))
    i += 1

print(a)

#if '%d%d' in a
