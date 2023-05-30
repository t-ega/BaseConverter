def to_decimal(number: int, given_base) -> int:
    return sum([int(digit) * (given_base ** index) for index, digit in enumerate(str(number)[::-1])])
