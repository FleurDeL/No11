# 정체불명의 첨탑들을 밀어 넘어뜨려서 부수기로 하였다.
# 첨탑은 일렬로 줄지어 서 있으며 산지니가 첨탑을 앞에서 밀면 뒤로 밀려 넘어진다.
# 밀려 넘어지는 첨탑의 높이가 바로 그다음 첨탑의 높이보다 클 때만 그다음 첨탑도 밀려 넘어진다.
# 모든 첨탑을 밀어 넘어뜨리기 위해서 몇 번을 밀어야 하는지 구하여라. 산지니는 반드시 앞으로만 이동하며 길을 우회하지 않는다.
# 첨탑의 높이는 1~9까지, 입력은 '1 3 5 4' 와 같이 입력된다
how_many = str(input('how many'))
how_many_times = int(len(how_many)/2)+1
times = 0
i = 0
for h in range(how_many_times-1):
    if how_many[i] > how_many[i+2]:
        times = times
    else:
        times += 1
    i += 2
    if i == how_many_times-2:
        if how_many[-3] >= how_many[-1]:
            times += 1
print(times)
print('for end')

if how_many[-3] < how_many[-1]:
    times += 1



print(times)
print(how_many)