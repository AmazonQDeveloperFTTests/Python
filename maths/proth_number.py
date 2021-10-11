"""

Calculates the nth Proth number

Source:
    https://handwiki.org/wiki/Proth_number

"""

import math


def proth(number: int) -> int:
    """
    :param number: nth number to calculate in the sequence
    :return: the nth number in Proth number

    Note: indexing starts at 1 i.e. proth(1) gives the first Proth number of 3

    >>> proth(6)
    25

    >>> proth(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input value of [number=-1] has to be > 0

    >>> proth(6.0)
    Traceback (most recent call last):
    ...
    TypeError: Input value of [number=6.0] has to be an integer
    """

    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] has to be an integer")

    if number < 1:
        raise ValueError(f"Input value of [number={number}] has to be > 0")
    elif number == 1:
        return 3
    elif number == 2:
        return 5
    else:
        block_index = number // 3
        """
        +1 for binary starting at 0 i.e. 2^0, 2^1, etc.
        +1 to start the sequence at the 3rd Proth number
        Hence, we have a +2 in the below statement
        """
        block_index = math.log(block_index, 2) + 2
        block_index = int(block_index)

        proth_list = [3, 5]
        proth_index = 2
        increment = 3
        for block in range(1, block_index):
            for move in range(increment):
                proth_list.append(2 ** (block + 1) + proth_list[proth_index - 1])
                proth_index += 1
            increment *= 2

    return proth_list[number - 1]


if __name__ == "__main__":
    print(f"The 6th Proth number: {proth(6)}")
