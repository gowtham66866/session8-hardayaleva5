## Session8 Assignment
***

 
### Run Test Cases

    $ pytest -vv

Above command runs all the test cases in local machine as defined in 
test_session8_assignment.py file.


### session8_assignment.py
***
> Session8 explains the usage of the scopes (global, local, nonlocal), closures and it's application in the real world scenario. It explains the cell object implementation and free variable concept.

> ### check_docstring
> Closure to check the no. of char in the docstring of the function passed. Returns True if more than 50 characters found in the docstring else False. This closure used the `char_len` as free variable holds the value `50`.

> ###  function_counter
> Closure to count the no. of times the function is `called` with
the user defined dictionary `input_dict` to store the values. This closure uses the free variables to hold the function & dictionary.

```
    >>> import session8_assignment as s8ast
    >>> test_dict = {}
    >>> function_count = s8ast.function_counter(print, test_dict)
    >>> function_count('test')
    test
    >>> function_count('function')
    function
    >>> function_count('assignment')
    assignment
    >>> test_dict
    {'print': 3}
    >>> 
```

> ### global_function_counter
> Closure to count the no. of times the function is `called` and the
value of the counter stored in the global dictionary `global_dict`. This closure uses the global variable to store the count.

```
    >>> import session8_assignment as s8ast
    >>> global_function = s8ast.global_function_counter(print)
    >>> global_function('test')
    test
    >>> global_function('hello')
    hello
    >>> global_function('world')
    world
    >>> s8ast.global_dict
    {'print': 3}
    >>> 
```

> ### next_fibonacci_number
> Closure to generate the fibonacci number. During the program execution
it hold the last two fibonacci numbers to find the next fibonacci number. This closure consists of two free variables which holds the last values of the fibonacci series.
 
```   
    >>> import session8_assignment as s8ast 
    >>> fibonacci_number = s8ast.next_fibonacci_number()
    >>> fibonacci_number()
    0
    >>> fibonacci_number()
    1
    >>> fibonacci_number()
    1
    >>> fibonacci_number()
    2
    >>> fibonacci_number()
    3
    >>> fibonacci_number()
    5
    >>> fibonacci_number()
    8
    >>> fibonacci_number()
    13
    >>> fibonacci_number()
    21
    >>> 
```  


***
> ## Unit test cases
***

> test_session8_assignment.py contains all the test cases for session8_assignment.py module.
This test cases covers the positive & negative cases like different input value for different scenario.
> Code coverage for the session8 module is of 100% which covers all the possible test cases.

> 
```

(base) BAN7183:session8-hardayaleva5 hsingh$ pytest -vv
=========================test session starts ========================================
platform darwin -- Python 3.6.8, pytest-4.5.0, py-1.8.0, pluggy-0.13.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/hsingh/session8-hardayaleva5
plugins: celery-4.3.0, arraydiff-0.3, cov-2.7.1, doctestplus-0.3.0, openfiles-0.3.2, remotedata-0.3.1
collected 15 items

test_session8_assignment.py::test_readme_exists PASSED                    [  6%]
test_session8_assignment.py::test_readme_contents PASSED                  [ 13%]
test_session8_assignment.py::test_readme_proper_description PASSED        [ 20%]
test_session8_assignment.py::test_readme_file_for_formatting PASSED       [ 26%]
test_session8_assignment.py::test_indentations PASSED                     [ 33%]
test_session8_assignment.py::test_function_name_had_cap_letter PASSED     [ 40%]
test_session8_assignment.py::test_min_test_cases PASSED                   [ 46%]
test_session8_assignment.py::test_function_doc_strings PASSED             [ 53%]
test_session8_assignment.py::test_check_docstring PASSED                  [ 60%]
test_session8_assignment.py::test_next_fibonacci_number PASSED            [ 66%]
test_session8_assignment.py::test_global_function_counter PASSED          [ 73%]
test_session8_assignment.py::test_function_counter PASSED                 [ 80%]
test_session8_assignment.py::test_invalid_check_docstring PASSED          [ 86%]
test_session8_assignment.py::test_invalid_global_function_counter PASSED  [ 93%]
test_session8_assignment.py::test_invalid_function_counter PASSED         [100%]

=========================15 passed in 0.06 seconds =====================================

```
***