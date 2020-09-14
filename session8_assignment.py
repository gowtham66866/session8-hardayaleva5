"""
session8_assignment.py
"""

global_dict = {}

def check_docstring():
    """
    Closure to check the no. of char in the docstring of the function
    passed. Returns True if more than 50 characters found in the docstring else
    false.
    """
    char_len = 50

    def count_chars(func):
        nonlocal char_len
        if not callable(func):
            raise ValueError("object not callable")
        return bool(func.__doc__ and (len(func.__doc__) >= char_len))

    return count_chars


def next_fibonacci_number():
    """
    Closure to generate the Fibonacci number. During the program execution
    it hold the last two fibonacci numbers to find the next fibonacci number.
    """
    old, new = 0, 1
    count = 0

    def fibonacci():
        nonlocal count
        nonlocal old, new
        if count == 0:
            count += 1
            return 0
        elif count == 1:
            count += 1
            return 1
        count += 1
        old, new = new, (old + new)
        return new

    return fibonacci


def global_function_counter(func):
    """
    Closure to count the no. of times the function is `called` and the
    value of the counter stored in the global dictionary `global_dict`.

    :param func: function to which the counter is to be bounded
    """
    global global_dict
    if not callable(func):
        raise ValueError("object not callable")

    def function_count(*args, **kwargs):
        if func.__name__ not in global_dict:
            global_dict[func.__name__] = 1
        else:
            global_dict[func.__name__] += 1
        return func(*args, **kwargs)

    return function_count


def function_counter(func, input_dict: dict):
    """
    Closure to count the no. of times the function is `called` with
    the user defined dictionary `input_dict` to store the values.

    :param func: function to count the execution
    :param input_dict: dictionary to hold the counter values
    """
    if not callable(func):
        raise ValueError("object not callable")
    if not isinstance(input_dict, dict):
        raise ValueError("not a valid datatype")

    def function_count(*args, **kwargs):
        nonlocal input_dict
        if func.__name__ not in input_dict:
            input_dict[func.__name__] = 1
        else:
            input_dict[func.__name__] += 1
        return func(*args, **kwargs)

    return function_count
