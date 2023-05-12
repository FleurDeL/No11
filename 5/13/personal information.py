def person(age):
    print('I am a person')
    def student(major):
        print('I like learning')
        def vacation(place):
            print('But I need to take breaks')
            print(age,'|',major,'|',place)
        return vacation                          #적절한 함수 반환하는 코드 한 줄
    return student                              #적절한 함수 반환하는 코드 한 줄


person(12)('math')('beach')