"""
Python implementation of the MSD radix sort algorithm
"""
from typing import List


def msd_radix_sort(list_of_ints: List[int]) -> List[int]:
    """
    Implementation of the MSD radix sort algorithm. Only works
    with positive integers
    :param list_of_ints: A list of integers
    :return: Returns the sorted list
    >>> msd_radix_sort([40, 12, 1, 100, 4])
    [1, 4, 12, 40, 100]
    >>> msd_radix_sort([])
    []
    >>> msd_radix_sort([123, 345, 123, 80])
    [80, 123, 123, 345]
    >>> msd_radix_sort([1209, 834598, 1, 540402, 45])
    [1, 45, 1209, 540402, 834598]
    """
    if not list_of_ints:
        return []

    if min(list_of_ints) < 0:
        raise ValueError("All numbers must be positive")

    most_bits = max(len(bin(x)[2:]) for x in list_of_ints)
    return _msd_radix_sort(list_of_ints, most_bits)


def _msd_radix_sort(list_of_ints: List[int], bit_position: int) -> List[int]:
    """
    Sort the given list based of the bit at bit_position. Numbers with a
    0 at that position will be at the start of the list, numbers with a
    1 at the end.
    :param list_of_ints: A list of integers
    :param bit_position: a bit which gets compared
    :return: Returns a list of integers
    """
    if bit_position == 0 or len(list_of_ints) == 1 or len(list_of_ints) == 0:
        return list_of_ints

    zeros = list()
    ones = list()
    # Split numbers based on bit at bit_position from the right
    for index, number in enumerate(list_of_ints):
        if (number >> (bit_position - 1)) & 1:
            # number as a one at bit bit_position
            ones.append(number)
        else:
            # number as a zero at bit bit_position
            zeros.append(number)

    # recursively split both lists further
    zeros = _msd_radix_sort(zeros, bit_position - 1)
    ones = _msd_radix_sort(ones, bit_position - 1)

    # recombine lists
    res = zeros
    res.extend(ones)

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
