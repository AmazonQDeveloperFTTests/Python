"""
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest increasing subsequence of a given sequence.

The problem is  :
Given an ARRAY, to find the longest and increasing sub ARRAY in that given ARRAY and return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return [10, 22, 33, 41, 60, 80] as output
"""


def longestSub(ARRAY):  # This function is recursive
    """
    >>> longestSub([7,6,3,4,9,21,45])
    [7,6,3,4,9,21,45]
    >>> longestSub([-1,5,7,-6,0,1,56])
    [-6,0,1,56]
    >>> longestSub([5,8,10,23,12,14,3])
    [5,8,10,12,14]
    >>> longestSub([34,21,45,67,32,12])
    [21,45,67] 
    """

    ARRAY_LENGTH = len(ARRAY)
    if (
        ARRAY_LENGTH <= 1
    ):  # If the array contains only one element, we return it (it's the stop condition of recursion)
        return ARRAY
        # Else
    PIVOT = ARRAY[0]
    isFound = False
    i = 1
    LONGEST_SUB = []
    while not isFound and i < ARRAY_LENGTH:
        if ARRAY[i] < PIVOT:
            isFound = True
            TEMPORARY_ARRAY = [element for element in ARRAY[i:] if element >= ARRAY[i]]
            TEMPORARY_ARRAY = longestSub(TEMPORARY_ARRAY)
            if len(TEMPORARY_ARRAY) > len(LONGEST_SUB):
                LONGEST_SUB = TEMPORARY_ARRAY
        else:
            i += 1

    TEMPORARY_ARRAY = [element for element in ARRAY[1:] if element >= PIVOT]
    TEMPORARY_ARRAY = [PIVOT] + longestSub(TEMPORARY_ARRAY)
    if len(TEMPORARY_ARRAY) > len(LONGEST_SUB):
        return TEMPORARY_ARRAY
    else:
        return LONGEST_SUB


# Some examples

print(longestSub([4, 8, 7, 5, 1, 12, 2, 3, 9]))
print(longestSub([9, 8, 7, 6, 5, 7]))
