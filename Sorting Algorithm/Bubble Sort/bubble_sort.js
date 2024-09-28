let arr = [64, 34, 25, 12, 22, 11, 90];
bubbleSort(arr);

function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            // Log current comparison
            console.log(`Comparing ${arr[j]} and ${arr[j + 1]}`);
            if (arr[j] > arr[j + 1]) {
                // Log swap
                console.log(`Swapping ${arr[j]} and ${arr[j + 1]}`);
                
                // -----> Swapping Values (Initializing Way) <-----
                // let temp = arr[j];
                // arr[j] = arr[j + 1];
                // arr[j + 1] = temp;

                // -----> Swapping Values (Destructuring Way) <-----
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
            }
        }
        // Log array state after each pass
        console.log(`Array after pass ${i + 1}:`, arr);
    }
}

