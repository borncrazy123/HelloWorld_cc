"""Bubble sort implementation."""


def bubble_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values using the bubble sort algorithm."""
    result = values.copy()

    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True

        if not swapped:
            break

    return result


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(numbers))
