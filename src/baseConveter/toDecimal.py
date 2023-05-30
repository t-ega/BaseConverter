from .availableBase import AvailableBase


def to_decimal(number: int, given_base) -> int:
    if given_base not in AvailableBase.availableBases():
        raise ValueError("Given base {} is not supported".format(given_base))

    return sum([int(digit) * (given_base ** index) for index, digit in enumerate(str(number)[::-1])])
