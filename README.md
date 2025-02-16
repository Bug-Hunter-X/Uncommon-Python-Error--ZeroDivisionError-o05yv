# Uncommon Python Error: ZeroDivisionError

This repository demonstrates a simple Python function that can lead to an uncommon error: `ZeroDivisionError`. The error occurs when the function attempts to divide by zero.

## The Bug

The function `function_with_uncommon_error` in `bug.py` has a conditional statement checking if `x` is equal to zero. If `x` is 0, it returns `1 / x`, causing a `ZeroDivisionError`. This is a common error, but it might not be immediately obvious to developers who are not familiar with the Python language or exception handling.