# in => 부분 문자열이 전체 문자열에 있는지 없는지만 알려주는 명령어
# 예, 아니요만 출력하기 떄문에 불리언 타입
a = 'abc123'
print('a' in a) # True
print('d' in a) # False
print('1*3' in a) # False => 문자열이기 때문에 연산 불가

# count() => 부분 문자열이 전체 문자열에서 몇 번이나 사용했는지 빈도를 출력
#부분 문자열이 서로 겹치는 경우는 처리 불가
fruit = 'ban'
print(fruit.count('ana')) # ana는 총 2개있지만 겹치기 떄문에 1이라는 결과

# replace() => 부분 문자열 바꾸기
print("variables have no spaces".replace(" ","_")) # 첫번째 문자열은 찾아야 하는 것, 두번째는 바꿀 것
