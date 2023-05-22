import sys
input = sys.stdin.readline

t = []
T = int(input())
for i in range(T):
    T = int(input())
    t.append(T)
t.sort()
for i in range(len(t)):
    print(t[i])
