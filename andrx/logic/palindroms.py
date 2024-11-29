# determinate if and input number is a palindrom

def is_palindrom(number):
    str_number = str(number)

    reverse_number = ''

    # for i in range(len(str_number) -1, -1, -1):
    #     reverse_number += str_number[i]

    for i in range(len(str_number)):
        reverse_number = str_number[i] + reverse_number

    # print(str_number[::-1])

    return reverse_number == str_number

def run_cases():
    number = input("Type a number: ")
    result = is_palindrom(number)

    print(result)

run_cases()