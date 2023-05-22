no = int(input())

count = 0
for _ in range(no):
    w = input()
    print(w)
    count += (list(w) == sorted(w, key=w.find))*1
    print(list(w.find))
print(count)