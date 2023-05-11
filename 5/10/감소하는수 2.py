number_found = ()
number = 0
for i in range(1000000):
    number_str = str(number)
    length_of_number = len(number_str)
    if length_of_number == 1:
        number_found = number_found + (number_str,)
        number += 1
        print(number)
    if length_of_number == 2:
        first_digit = number_str[0]
        second_digit = number_str[1]
        if first_digit > second_digit:
            number_found = number_found + (number_str,)
        number += 1
    if length_of_number == 3:
        number_str = str(number)
        first_digit = number_str[0]
        second_digit = number_str[1]
        third_digit = number_str[2]
        if first_digit > second_digit and second_digit > third_digit:
            number_found = number_found + (number_str,)
        number += 1
    if length_of_number == 4:
        number_str = str(number)
        first_digit = number_str[0]
        second_digit = number_str[1]
        third_digit = number_str[2]
        fourth_digit = number_str[3]
        if first_digit > second_digit and second_digit > third_digit and third_digit > fourth_digit:
            number_found = number_found + (number_str,)
        number += 1
    if length_of_number == 5:
        number_str = str(number)
        first_digit = number_str[0]
        second_digit = number_str[1]
        third_digit = number_str[2]
        fourth_digit = number_str[3]
        fifth_digit = number_str[4]
        if first_digit > second_digit and second_digit > third_digit and third_digit > fourth_digit \
                and fourth_digit > fifth_digit:
            number_found = number_found + (number_str,)
        number += 1

        if length_of_number == 5:
            number_str = str(number)
            first_digit = number_str[0]
            second_digit = number_str[1]
            third_digit = number_str[2]
            fourth_digit = number_str[3]
            fifth_digit = number_str[4]
            if first_digit > second_digit and second_digit > third_digit and third_digit > fourth_digit \
                    and fourth_digit > fifth_digit:
                number_found = number_found + (number_str,)
            number += 1

        if length_of_number == 6:
            number_str = str(number)
            first_digit = number_str[0]
            second_digit = number_str[1]
            third_digit = number_str[2]
            fourth_digit = number_str[3]
            fifth_digit = number_str[4]
            sixth_digit = number_str[5]
            if first_digit > second_digit and second_digit > third_digit and third_digit > fourth_digit \
                    and fourth_digit > fifth_digit and fifth_digit > sixth_digit:
                number_found = number_found + (number_str,)
            number += 1
        if length_of_number == 7:
            number_str = str(number)
            first_digit = number_str[0]
            second_digit = number_str[1]
            third_digit = number_str[2]
            fourth_digit = number_str[3]
            fifth_digit = number_str[4]
            sixth_digit = number_str[5]
            seventh_digit = number_str[6]
            if first_digit > second_digit and second_digit > third_digit and third_digit > fourth_digit \
                    and fourth_digit > fifth_digit and fifth_digit > sixth_digit and sixth_digit > seventh_digit:
                number_found = number_found + (number_str,)
            number += 1
print(len(number_found))
N_th_number = int(input('몇 번째 감소하는 수를 찾으십니까'))
if N_th_number < 0:
    print('음의 자리')
else:
    print(number_found[N_th_number])
