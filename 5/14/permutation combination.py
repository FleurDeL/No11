from itertools import permutations # 순열 : 서로다른 n개에서 r개를 뽑을때 순서 신경쓰면서 중복없이 뽑기
from itertools import combinations # 조합 : 순서 신경안쓰고 중복없이 r개 뽑기
from itertools import product #product : 두개 이상 리스트에서 모든 조합 구하기
arr = ['a', 'b', 'c', 'd']
print(permutations(arr, 2)) #리스트나 튜플이 아니기때문에 출력안됨
for i in permutations(arr, 2):
    print(i)


arr = ['a', 'b', 'c', 'd']
print(combinations(arr, 2)) #리스트나 튜플이 아니기때문에 출력안됨
for i in combinations(arr, 2):
    print(i)

#리스트나 튜플로 만들어주기
print(list(combinations(arr, 2)))

print(list(permutations(arr, 2)))


items = [[1,2,3],[4,5,6]]
items_1 = [1,2,3]; items_2 = [4,5,6]
product_list = list(product(*items_2))
print('k')
print(product_list)