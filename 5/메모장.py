def count_substring(main_string, sub_string):
    count = 0
    start = 0
    while True:
        index = main_string.find(sub_string, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count

a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
T = 'ddz=z='

print(count_substring(T,a))