def fizz_buzz_v1(start, end):

    """
    Typical test interview question using simple if, elif else control flow. 
    Returns a string based on the "start" and "end" values provided,
    replacing specific values with the following:

    Multiples of 5 and 3 are replaced with "FizzBuzz",
    Multiples of 5 are replaced with "Buzz",
    Multiples of 3 are replaced with "Fizz",
    Any numbers not divisible by 3, 5 or both are replaced with the string version of themselves

    Note - +1 is added to the "end" parameter to include it in the return string

    Params:
        start (int): The start of the range
        end (int): The end of the range

    Returns:
        str: A comma-separated string, for example "1,2,Fizz,4,Buzz,Fizz"
    """

    result = []

    for i in range(start, end + 1):
        if i % 5 == 0 and i % 3 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(i))

    return ",".join(result)


def fizz_buzz_v2(start, end):

    """
    Typical test interview question using a (rather silly) list comprehension. 
    Returns a string based on the "start" and "end" values provided,
    replacing specific values with the following:

    Multiples of 5 and 3 are replaced with "FizzBuzz",
    Multiples of 5 are replaced with "Buzz",
    Multiples of 3 are replaced with "Fizz",
    Any numbers not divisible by 3, 5 or both are replaced with the string version of themselves

    Note - +1 is added to the "end" parameter to include it in the return string

    Params:
        start (int): The start of the range
        end (int): The end of the range

    Returns:
        str: A comma-separated string, for example "1,2,Fizz,4,Buzz,Fizz"
    """

    return ",".join(
        [
            "FizzBuzz" * (i % 5 == 0 and i % 3 == 0)
            or "Buzz" * (i % 5 == 0)
            or "Fizz" * (i % 3 == 0)
            or str(i)
            for i in range(start, end + 1)
        ]
    )
