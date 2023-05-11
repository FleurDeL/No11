
number_found = ()
number = 0
for i in range(1000):
    if number < 10:
        number_str = str(number)
        number_found = number_found + (number_str,)
        number += 1
    if number >= 10 and number < 100:
        number_str = str(number)
        first_digit = number_str[0]
        second_digit = number_str[1]
        if first_digit > second_digit:
            number_found = number_found + (number_str,)
        number += 1
    if number >= 100 and number < 1000:
        number_str = str(number)
        first_digit = number_str[0]
        second_digit = number_str[1]
        third_digit = number_str[2]
        if first_digit > second_digit and second_digit > third_digit:
            number_found = number_found + (number_str,)
        number += 1
print(number_found)

N_th_number = int(input('몇 번째 감소하는 수를 찾으십니까'))
print(number_found[N_th_number])