from __future__ import annotations


def knuth_morris_pratt(pattern: str, text: str) -> int:
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)

    1) Preprocess pattern to identify any suffixes that are identical to prefixes

        This tells us where to continue from if we get a mismatch between a character
        in our pattern and the text.

    2) Step through the text one character at a time and compare it to a character in
        the pattern updating our location within the pattern if necessary

    >>> kmp = "knuth_morris_pratt"
    >>> knuth_morris_pratt(kmp, "kn") == kmp.find("kn")
    True
    >>> knuth_morris_pratt(kmp, "h_m") == kmp.find("h_m")
    True
    >>> knuth_morris_pratt(kmp, "rr") == kmp.find("rr")
    True
    >>> knuth_morris_pratt(kmp, "tt") == kmp.find("tt")
    True
    >>> knuth_morris_pratt(kmp, "not there") == kmp.find("not there")
    True

    # A condensed version...
    >>> all(knuth_morris_pratt(kmp, s) == kmp.find(s) for s in (
    ...     "kn", "h_m", "rr", "tt", "not there"
    ... ))
    True
    """

    # 1) Construct the failure array
    failure = get_failure_array(pattern)

    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return i - j
            j += 1

        # if this is a prefix in our pattern
        # just go back far enough to continue
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return -1


def get_failure_array(pattern: str) -> list[int]:
    """
    Calculates the new index we should go to if we fail a comparison
    :param pattern:
    :return:
    """
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure


if __name__ == "__main__":
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    print(knuth_morris_pratt(pattern, text1), knuth_morris_pratt(pattern, text2))

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    print(knuth_morris_pratt(pattern, text))

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    print(knuth_morris_pratt(pattern, text))

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    print(knuth_morris_pratt(pattern, text))

    # Test 5)
    pattern = "aabaabaaa"
    assert get_failure_array(pattern) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
