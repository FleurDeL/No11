def area(shape, n):
    return shape(n)                 # 매개변수로 넓이를 계산하는 함수 shape와 값n을 입력받아서 넓이를 계산하는 코드 한 줄

def circle(radius):
    return 3.14*radius**2
def square(length):
    return length*length

print(area(circle,5))

print(area(circle,10))
print(area(square, 5))
