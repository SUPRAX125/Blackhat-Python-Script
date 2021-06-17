def sum(one, two):
    int_one = convert_integer(one)
    int_two = convert_integer(two)

    result = int_one + int_two

    return result

def convert_integer(number_string):
    integer = int(number_string)

    return integer

print(sum("1","4"))