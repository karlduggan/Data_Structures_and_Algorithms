def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr
arr = [8,7,5,3,2,4,9,7,5,3,4,5,3,8,9,6,5,4,3]

print(insertion_sort(arr))
    
    