def bubbleSort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array:", arr)
