def selectionSort(arr):
    n = len(arr)

    # Traverse through the unsorted part of the array
    for i in range(n - 1):
        # Assume the minimum is the first unsorted element
        minIndex = i

        # Find the actual minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted array:", arr)
