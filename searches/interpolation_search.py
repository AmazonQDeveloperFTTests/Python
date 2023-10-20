"""
This is pure Python implementation of interpolation search algorithm
"""


def interpolation_search(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of interpolation search algorithm in Python
    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    >>> interpolation_search([-1, 0, 1], -1)
    0
    >>> interpolation_search([-1, 0, 1], 2) == None
    True
    >>> interpolation_search([], -1) == None
    True
    >>> interpolation_search((-1, 0, 1), 0)
    1
    >>> interpolation_search(range(100), 99)
    99
    >>> interpolation_search({-1, 0, 1}, -1)
    Traceback (most recent call last):
        ...
    TypeError: 'set' object is not subscriptable
    >>> interpolation_search([-1.0, 0, 1], -1.0)
    Traceback (most recent call last):
        ...
    TypeError: list indices must be integers or slices, not float
    >>> interpolation_search(["A", "B", "C"], "C")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    >>> interpolation_search({1:4, 2:9, 0:42}, 1) == None
    True
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        # avoid divided by 0 during interpolation
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            else:
                return None

        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        # out of range check
        if point < 0 or point >= len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if point < left:
                right = left
                left = point
            elif point > right:
                left = right
                right = point
            else:
                if item < current_item:
                    right = point - 1
                else:
                    left = point + 1
    return None


def interpolation_search_by_recursion(sorted_collection: list[int], item: int, left: int, right: int) -> int | None:
    """Pure implementation of interpolation search algorithm in Python by recursion
    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    >>> interpolation_search_by_recursion(
    ... [-1, 0, 1], -1, 0, 2
    ... )
    0
    >>> interpolation_search_by_recursion(
    ... [-1, 0, 1], 2, 0, 2
    ... ) == None
    True
    >>> interpolation_search_by_recursion(
    ... [], -1, 0, 0
    ... ) == None
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> interpolation_search_by_recursion(
    ... (-1, 0, 1), 0, 0, 2
    ... )
    1
    >>> interpolation_search_by_recursion(
    ... range(100), 99, 0, 99
    ... )
    99
    >>> interpolation_search_by_recursion(
    ... {-1, 0, 1}, -1, 0, 2
    ... )
    Traceback (most recent call last):
        ...
    TypeError: 'set' object is not subscriptable
    >>> interpolation_search_by_recursion(
    ... [-1.0, 0, 1], -1.0, 0, 2
    ... )
    Traceback (most recent call last):
        ...
    TypeError: list indices must be integers or slices, not float
    >>> interpolation_search_by_recursion(
    ... ["A", "B", "C"], "C", 0, 2
    ... )
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    >>> interpolation_search_by_recursion(
    ... {1:4, 2:9, 0:42}, 1, 0, 2
    ... ) == None
    True
    """

    # avoid divided by 0 during interpolation
    if sorted_collection[left] == sorted_collection[right]:
        if sorted_collection[left] == item:
            return left
        else:
            return None

    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # out of range check
    if point < 0 or point >= len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    elif point < left:
        return interpolation_search_by_recursion(sorted_collection, item, point, left)
    elif point > right:
        return interpolation_search_by_recursion(sorted_collection, item, right, left)
    else:
        if sorted_collection[point] > item:
            return interpolation_search_by_recursion(
                sorted_collection, item, left, point - 1
            )
        else:
            return interpolation_search_by_recursion(
                sorted_collection, item, point + 1, right
            )


def __assert_sorted(collection):
    """Check if collection is ascending sorted, if not - raises :py:class:`ValueError`
    :param collection: collection
    :return: True if collection is ascending sorted
    :raise: :py:class:`ValueError` if collection is not ascending sorted
    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True
    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
        ...
    ValueError: Collection must be ascending sorted
    """
    if collection != sorted(collection):
        raise ValueError("Collection must be ascending sorted")
    return True


if __name__ == "__main__":
    import sys

    """
        user_input = input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be ascending sorted to apply interpolation search')

    target_input = input('Enter a single number to be found in the list:\n')
    target = int(target_input)
        """

    debug = 0
    if debug == 1:
        collection = [10, 30, 40, 45, 50, 66, 77, 93]
        try:
            __assert_sorted(collection)
        except ValueError:
            sys.exit("Sequence must be ascending sorted to apply interpolation search")
        target = 67

    result = interpolation_search(collection, target)
    if result is not None:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
