# Arithmetic Arranger
A Python script to format and solve basic arithmetic problems (addition and subtraction) in a clean, vertically aligned layout.

## Features
- **Problem Formatting**: Displays up to 5 arithmetic problems (e.g., "32 + 698") in a neat, vertical format.
- **Error Handling**: Validates inputs for:
  - Maximum 5 problems.
  - Only digits in numbers (no letters or symbols).
  - Numbers up to 4 digits.
  - Only `+` or `-` operators.
- **Optional Answers**: Show the results of calculations if `show_answers=True`.
- **Clean Output**: Aligns numbers and operators with proper spacing and dashes for readability.

## Usage
Pass a list of arithmetic problems as strings, with an optional boolean to show answers:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
```
Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

## How It Works
- **Input Parsing**: Takes a list of problems in the format "num1 operator num2" (e.g., "32 + 698").
- **Validation**: Checks for valid operators (`+`, `-`), digit-only numbers, and number length (≤ 4 digits).
- **Formatting**: Aligns each problem vertically with proper spacing and dashes.
- **Answer Calculation**: Computes results for addition or subtraction if `show_answers=True`.
- **Output**: Returns a formatted string with or without answers based on the input parameter.

## Notes
- Input problems must be strings in the format `"num1 operator num2"` with spaces.
- Maximum of 5 problems allowed to keep output clean.
- Built with ❤️ by Ehsan for quick arithmetic formatting and calculations.
