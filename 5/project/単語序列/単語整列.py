a = []
T = list(map(str, input().split("\n")))
for _ in range(int(T[0])):  # 단어 하나씩 분리해서 리스트 생성
    T = list(map(str, input().split()))
    a.append(T[0])

overlap = [[] for _ in range(50)]  # 길이가 1부터 50까지인 단어들 넣을 리스트 생성

for i in range(50):  # 길이가 50까지
    for j in range(len(a)):  # 리스트 안의 단어들 모두 스캔
        if len(a[j]) == i + 1 and a[j] not in overlap[i]:  # 중복확인해서 리스트에 넣기
            overlap[i].append(a[j])

for k in range(len(overlap)):  # 알파벳 순으로 정렬
    overlap[k].sort()

for l in range(len(overlap)):  # 출력
    for m in range(len(overlap[l])):
        print(overlap[l][m])
