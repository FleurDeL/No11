a = []
T = list(map(str, input().split("\n")))
for _ in range(int(T[0])):
    T = list(map(str, input().split()))
    a.append(T[0])
print(a)
a.sort()
print(a)
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_ = [list_1,list_2,list_3,list_4,list_5,list_6]
overlap = []
for i in range(len(a)):
        if len(a[i]) == 1:
            if a[i] not in list_1:
                list_1.append(a[i])
        elif len(a[i]) == 2:
            if a[i] not in list_2:
                list_2.append(a[i])
        elif len(a[i]) == 3:
            if a[i] not in list_3:
                list_3.append(a[i])
        elif len(a[i]) == 4:
            if a[i] not in list_4:
                list_4.append(a[i])
        elif len(a[i]) == 5:
            if a[i] not in list_5:
                list_5.append(a[i])
        elif len(a[i]) == 6:
            if a[i] not in list_6:
                list_6.append(a[i])


for j in range(len(list_)):
        for k in range(len(list_[j])):
            print(list_[j][k])