def countingSort(arr, shift, mask):
    if not arr:
        return arr
    
    n = len(arr)
    output = [0] * n
    count = [0]* (mask + 1)
    
    for num in arr:
        index = (num >> shift) & mask
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (arr[i] >> shift) & mask
        count[index] -= 1
        output[count[index]] = arr[i]

    return output
    