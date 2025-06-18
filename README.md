# MathCalculator

A simple Python package for basic mathematical operations.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers (with zero-division protection)

## Installation

### Install from PyPI
```bash
pip install mathcalculator-bracken576
```

### Install from Source
```bash
git clone https://github.com/bracken576/mathcalculator.git
cd mathcalculator
pip install .
```

## Usage

```python
from mathcalculator import MathCalculator_bracken576

# Initialize the calculator
calc = MathCalculator()

# Perform operations
result_add = calc.add(5, 3)        # Returns 8
result_sub = calc.subtract(10, 4)  # Returns 6
result_mul = calc.multiply(3, 7)   # Returns 21
result_div = calc.divide(15, 3)    # Returns 5.0

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")
```

## Building and Testing the Package

### Local Installation and Testing

1. **Install the package locally:**
   ```bash
   pip install .
   ```

2. **Install with development dependencies:**
   ```bash
   pip install -e .[dev]
   ```

3. **Run tests:**
   ```bash
   pytest tests/
   ```