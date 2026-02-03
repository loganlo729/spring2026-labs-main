from __future__ import annotations

def uniques_in_order(nums: list[int]) -> list[int]:
    """Return a list of the unique elements in nums, in the order they first appear.

    >>> uniques_in_order([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    >>> uniques_in_order([5, 5, 5, 5])
    [5]
    >>> uniques_in_order([])
    []
    >>> uniques_in_order([1, 2, 3])
    [1, 2, 3]
    """
    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_nums.append(num)
    return unique_nums
