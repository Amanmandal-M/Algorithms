function selectionSort(arr) {
    let n = arr.length;

    // Traverse through the unsorted part of the array
    for (let i = 0; i < n - 1; i++) {
        // Assume the minimum is the first unsorted element
        let minIndex = i;

        // Find the actual minimum element in the unsorted part
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        // Swap the found minimum with the first unsorted element
        let temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

// Example usage:
let arr = [64, 25, 12, 22, 11];
selectionSort(arr);
console.log("Sorted array:", arr);
