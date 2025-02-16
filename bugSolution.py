def function_with_uncommon_error(x, y):
    if x == 0:
        return float('inf') # Return positive infinity instead of raising an error
    return x + y

result = function_with_uncommon_error(0, 5) #Return positive infinity
print(result)

#Alternative solution: using try-except block to handle the error
def function_with_uncommon_error_try_except(x, y):
    try:
        return 1 / x
    except ZeroDivisionError:
        return float('inf')

result_try_except = function_with_uncommon_error_try_except(0,5) #Return positive infinity
print(result_try_except) 