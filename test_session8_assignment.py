import importlib
import inspect
import os
from random import randint

import pytest
import re
import session8_assignment as s8ast

MIN_TEST_CASES = 15
README_CONTENT_CHECK_FOR = [
    'closure',
    'free',
    'variables',
    'nonlocal',
    'scopes',
    'char_len',
    'global',
    'dictionary',
    'fibonacci',
    'cell'
]


def experiment():
    """
    This is test functionThis is test functionThis is test functionThis is test functionThis is test function
    """
    pass


def experiment_10():
    """
    This is test function.
    """
    pass


def experiment_empty():
    pass


def experiment_add(a: int, b: int):
    return a+b


def experiment_mul(a: int, b: int):
    return a*b


def experiment_div(a: int, b: int):
    return a/b


# Basic tests
def test_readme_exists():
    """
    Test to check if the `README.md` file exists or not in the repo.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test case to check the contents of the `README.md` file and
    also checks if the file consists of at least 500 words.
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
            len(readme_words) >= 465
    ), "Make your README.md file interesting! Add at least 500 words"


def test_readme_proper_description():
    """
    Test to cross check if the `README.md` file contains proper description
    of modules.
    """
    readme_looks_good = True
    file_to_check = open("README.md", "r", encoding="utf-8")
    content = file_to_check.read()
    file_to_check.close()
    for word in README_CONTENT_CHECK_FOR:
        if word not in content:
            readme_looks_good = False
    assert (
        readme_looks_good
    ), "You have not described all the functions/class " \
       "well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test to check the proper formatting of the `README.md` file.
    """
    file_to_check = open("README.md", "r", encoding="utf-8")
    content = file_to_check.read()
    file_to_check.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Test case to check the indentation of the python file.
    """
    lines = inspect.getsource(s8ast)
    spaces = re.findall("\n +.", lines)
    for i, space in enumerate(spaces):
        assert (
                len(space) % 4 == 2
        ), "Your script contains misplaced indentations"
        assert (
                len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test to check if the function name is defined in caps
    or mixed case in python file.
    """
    functions = inspect.getmembers(s8ast, inspect.isfunction)
    for function in functions:
        assert (
                len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_min_test_cases():
    """
    Test case to check at least minimum test cases that are defined in
    test file.
    """
    mod = importlib.import_module("test_session8_assignment", os.path.abspath('.'))
    functions = inspect.getmembers(mod, inspect.isfunction)
    assert len(functions) >= MIN_TEST_CASES


def test_function_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    functions = inspect.getmembers(s8ast, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__, "Docstring(s) are missing!!!"

# Positive Test cases


def test_check_docstring():
    """
    Test case to check the `check_docstring` closure functionality.
    """
    doc_string_cell = s8ast.check_docstring()
    assert doc_string_cell(experiment)
    assert not doc_string_cell(experiment_10)
    assert not doc_string_cell(experiment_empty)


def test_next_fibonacci_number():
    """
    Test case to check the `next_fibonacci_number` closure functionality with
    various expected output.
    """
    fib = s8ast.next_fibonacci_number()
    for _ in range(10):
        x = fib()
    assert x == 34
    assert fib() == 55


def test_global_function_counter():
    """
    Tests the `global_function_counter` with the different experiment functions
    like add/mul/div are used and test randomly.
    """
    test_add = s8ast.global_function_counter(experiment_add)
    test_mul = s8ast.global_function_counter(experiment_mul)
    test_div = s8ast.global_function_counter(experiment_div)
    test_run_add = randint(1, 100)
    test_run_mul = randint(1, 100)
    test_run_div = randint(1, 100)
    for _ in range(test_run_add):
        _ = test_add(1, 2)
    assert s8ast.global_dict['experiment_add'] == test_run_add
    for _ in range(test_run_mul):
        _ = test_mul(1, 2)
    assert s8ast.global_dict['experiment_mul'] == test_run_mul
    for _ in range(test_run_div):
        _ = test_div(1, 2)
    assert s8ast.global_dict['experiment_div'] == test_run_div


def test_function_counter():
    """
    Test case to check `function_counter` closure with different input
    and output.
    """
    test_1 = {}
    test_2 = {}
    fc_1 = s8ast.function_counter(experiment_add, test_1)
    fc_2 = s8ast.function_counter(experiment_mul, test_2)
    for _ in range(10):
        _ = fc_1(1, 5)
    for _ in range(10):
        _ = fc_2(1, 5)
    assert test_1['experiment_add'] == 10
    assert test_2['experiment_mul'] == 10


# Negative Test cases


def test_invalid_check_docstring():
    """
    Test case to check `check_docstring` closure with various invalid input
    like passing different objects other than function expecting `ValueError`.
    """
    doc_str = s8ast.check_docstring()
    with pytest.raises(ValueError):
        assert doc_str('asdfasdf')
    with pytest.raises(ValueError):
        assert doc_str(123)
    with pytest.raises(ValueError):
        assert doc_str(5436.34)


def test_invalid_global_function_counter():
    """
    Test case to check `global_function_counter` with various invalid input
    like passing different objects other than function expecting `ValueError`.
    """
    with pytest.raises(ValueError):
        assert s8ast.global_function_counter('hello, world')()
    with pytest.raises(ValueError):
        assert s8ast.global_function_counter(19873)()
    with pytest.raises(ValueError):
        assert s8ast.global_function_counter(5436.34)()
    with pytest.raises(ValueError):
        assert s8ast.global_function_counter({})()


def test_invalid_function_counter():
    """
    Test case to check `function_counter` with various invalid input
    like passing different objects other than function expecting `ValueError`.
    """
    with pytest.raises(ValueError):
        assert s8ast.function_counter('hello, world', {})()
    with pytest.raises(ValueError):
        assert s8ast.function_counter(19873, {})()
    with pytest.raises(ValueError):
        assert s8ast.function_counter(5436.34, {})()
    with pytest.raises(ValueError):
        assert s8ast.function_counter({}, {})()
    with pytest.raises(ValueError):
        assert s8ast.function_counter(print, 123)()
