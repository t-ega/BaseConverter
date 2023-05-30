# Base Conversion Tool

The Base Conversion Tool is a Python library that provides functions for converting numbers from one base to another. Currently, the tool supports conversion between the following bases: 2, 3, 4, 8, 10, and 16.

## Installation

To use the Base Conversion Tool, you can simply download the `baseConverter.py` file and import it into your Python project. The tool has no external dependencies.

## Usage

The Base Conversion Tool provides two main functions: `digit_converter()` and `to_decimal()`. Here's how you can use them:

### digit_converter()

The `digit_converter()` gotten from the `baseConverter file` function can be used to convert a number from one base to another. Here's its signature:

```python
def digit_converter(number: int, input_base=10, output_base=None)
```

The `input_base` parameter specifies the base of the input number. If the input_base is not given a default base of 10 is assumed. The `number` parameter is the number to be converted, and should be an integer. The `output_base` parameter specifies the base to convert the number to. If `output_base` is not specified, the function returns the number in decimal format.

Here's an example of how to use `digit_converter()`:

```python
from base_conversion import digit_converter

# Convert binary number '1010' to octal
result = digit_converter('1010',2, 8)
print(result)
output = 12
```

## License

The Base Conversion Tool is released under the MIT License. See LICENSE file for details.

## Contributing

If you find a bug or have a suggestion for improvement, please open an issue on the GitHub repository. Pull requests are welcome!

## Acknowledgements

The Base Conversion Tool was inspired by similar tools available in other programming languages, such as the `bin()` and `hex()` functions in Python.

## Contact

For any questions or inquiries, please contact me at beniyoke@gmail.com.