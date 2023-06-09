from .availableBase import AvailableBase


def to_base(number: int, output_base):
    output = ''

    if output_base not in AvailableBase.availableBases():
        raise ValueError("Output base {} is not supported".format(output_base))

    while number != 0:
        carry = int(number) % output_base
        output += str(carry) if carry < 9 else {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}.get(carry, None)
        number = int(number) // output_base
    return output[::-1]

