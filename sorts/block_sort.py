def block_sort(lst: list) -> list:
    """
    Sorts a list using the Block Sort algorithm.

    The Block Sort algorithm works by dividing the input list into blocks of size
    sqrt(n), sorting each block, and then merging the sorted blocks into a single
    sorted list.

    Args:
        lst (list[int]): The unsorted list to be sorted.

    Returns:
        list[int]: The sorted list.

    Examples:
        >>> block_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        >>> block_sort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> block_sort([])
        []
    """
    if not lst:
        return []

    block_size = int(len(lst) ** 0.5)
    blocks = [lst[i : i + block_size] for i in range(0, len(lst), block_size)]
    for block in blocks:
        block.sort()

    sorted_lst = []
    while blocks:
        min_block = min(blocks, key=lambda x: x[0])
        sorted_lst.append(min_block.pop(0))
        if not min_block:
            blocks.remove(min_block)

    return sorted_lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()
