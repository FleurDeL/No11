#find() 대소문자 구분하면서 부분 문자열 검색
#"문자열".find('')의 형식 => "문자열"에서 ''안의 문자열 찾음 => 일치하는 부분의 문자열 인덱스 출력

print("some_string".find('ing')) # => 8
print("some_string".find('')) # => 0 빈 문자열은 어디서든 찾을 수 있기 때문

#역방향으로 찾고 싶을 때는 rfind() (r이 역방향(reverse)라는 뜻)
#문자열의 맨 뒤부터 검색하여 찾은 문자열의 0부터 시작하는 양수 인덱스 출력

who = "me myself and I"

print(who.find('you')) # => -1 해당 문자열이 없기 때문
print(who.find("e")) # => 1 해당 문자열이 있는 첫 번째 위치의 인덱스