a = str(input('승객 수'))
list = a.split('\n')
split = list[0].find(' ')
_out = list[0][0:split]
_in = list[0][split+1:]

passengers = 0
_max = 0
times = 0
for i in list:
    split = list[times].find(' ')
    _out = int(list[times][0:split])
    _in = int(list[times][split + 1:])
    before = passengers
    passengers = passengers - _out + _in
    after = passengers
    if _max < after:
        _max = after
    times += 1

print(_max)




