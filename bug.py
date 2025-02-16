def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    return x + y

result = function_with_uncommon_error(0, 5)