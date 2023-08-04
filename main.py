def quicksort(arr: list) -> list:
    """
    Performs an iterative (non-recursive) quicksort in Python
    """

    if len(arr) <= 1:
        return arr

    stack = []
    stack.append((0, len(arr) - 1))

    while stack:
        low, high = stack.pop()
        pivot_idx = partition(arr, low, high)

        if low < pivot_idx - 1:
            stack.append((low, pivot_idx - 1))
        if pivot_idx + 1 < high:
            stack.append((pivot_idx + 1, high))

    return arr

def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage; this will only execute if you run `main.py`
if __name__ == "__main__":
    import random

    n = 10 # Number of random numbers (exclusive)
    numbers = [int(random.random() * 100) for x in range(n)]
    print(quicksort(numbers))
