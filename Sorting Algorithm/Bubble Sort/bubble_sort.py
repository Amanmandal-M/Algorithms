arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Log current comparison
            print(f"Comparing {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                # Log swap
                print(f"Swapping {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # Log array state after each pass
        print(f"Array after pass {i + 1}: {arr}")

