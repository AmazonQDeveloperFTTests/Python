def last_digit_of_pow(number1: int, number2: int) -> int:

    """
    adding a last_digit_of_power algorithm 
    which returns the last digit of: 
    number1 to the power of number2
    
    >>> last_digit_of_pow(63, 6)
    9
    >>> last_digit_of_pow(724, 67521)
    4
    >>> last_digit_of_pow(230912350294580923559235802932358, 2034982093849324290348029429391)
    2
    """

    return pow(number1, number2, 10)


if __name__ == "__main__":
    __import__("doctest").testmod()
