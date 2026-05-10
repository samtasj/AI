def selectionSort(arr):
    n = len(arr)
    print("Original Array:", arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print(f"Step {i+1}: {arr}")

    print("Sorted Array:", arr)


# Main
arr = list(map(int, input("Enter elements: ").split()))
selectionSort(arr)