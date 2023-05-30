from toBase import to_base
from toDecimal import to_decimal


def digit_converter(number, input_base=10, output_base=None):
    available_base = [2, 3, 4, 8, 16, 10]

    if input_base not in available_base:
        raise ValueError('conversion in base {} is not supported'.format(input_base))

    if output_base not in available_base:
        raise ValueError('conversion to base {} is not supported'.format(output_base))

    try:
        # input type might not be a string
        int(number)
    except ValueError:
        raise ValueError('Number {} is not a digit'.format(number))

    if input_base != 10:
        # convert to decimal
        number = to_decimal(number, 2)
        # convert the decimal to the required base
        return to_base(number, output_base=output_base)
    else:
        return to_base(number, output_base=output_base)

result = digit_converter(1010,2, )
print(result)