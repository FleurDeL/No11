print('left or right')

do = input(":: ")
if do == 'left' :
    print('crab or starfish')
    do = input(":: ")
    if do == 'crab' :
        print('yes or no')
        do = input(":: ")
        if do == 'yes' :
            print('yes or no')
            do = input(":: ")
            if do == 'no' :
                print(':)')
            else : print(':(')
        else: print(':(')
    else: print(':(')
else : print(':(')