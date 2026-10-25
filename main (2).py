"""
Python Recursion Practice

A collection of recursive functions written while learning recursion.
Each function focuses on a specific problem or pattern.
"""


def count_down(n: int) -> None:
    """Print a countdown from n to 1, followed by 'Done!'."""
    if n == 1:
        print(n)
        print("Done!")
        return

    print(n)
    count_down(n - 1)


def recursive_sum(n: int) -> int:
    """Return the sum of integers from 1 to n."""
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


def sum_digits(n: int) -> int:
    """Return the sum of the digits of a non-negative integer."""
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


def reverse_string(text: str) -> str:
    """Return text in reverse order using recursion."""
    if len(text) == 0:
        return text
    return text[-1] + reverse_string(text[:-1])


def is_palindrome(text: str) -> bool:
    """Return whether text is a palindrome."""
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def list_sum(numbers: list[int]) -> int:
    """Return the sum of all integers in a list."""
    if len(numbers) == 0:
        return 0
    return numbers[-1] + list_sum(numbers[:-1])


def count_occurrences(numbers: list[int], target: int, index: int = 0, count: int = 0) -> int:
    """Count how many times target appears in numbers."""
    if index == len(numbers):
        return count

    if numbers[index] == target:
        count += 1

    return count_occurrences(numbers, target, index + 1, count)


def is_sorted(numbers: list[int], index: int = 0) -> bool:
    """Return whether numbers are sorted in non-decreasing order."""
    if len(numbers) <= 1 or index == len(numbers) - 1:
        return True

    if numbers[index] > numbers[index + 1]:
        return False

    return is_sorted(numbers, index + 1)


def binary_search(numbers: list[int], target: int, left: int, right: int) -> int:
    """
    Return the index of target in a sorted list, or -1 if it is absent.

    The right boundary is inclusive.
    """
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle
    if numbers[middle] > target:
        return binary_search(numbers, target, left, middle - 1)
    return binary_search(numbers, target, middle + 1, right)

