n=int(input());l=list(map(int,input().split()))
print(n,l)
for i in l:
    print(i,l)
    r = 0
    for j in range(1,i):
        if i%j==0:r=j
    if r!=1:n-=1
print(n)
