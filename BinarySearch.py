def binarysearch(arr, n, k):
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == k:
            return mid  # Target found, return index
        elif mid_value < k:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found

arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 4

result = binarysearch(arr, n, k)

if result != -1:
    print("Output: " + str(result))
else:
    print("Output: " + str(result))



        
        

        
        


binarysearch(arr, n, k)