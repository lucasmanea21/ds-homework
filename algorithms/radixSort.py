from algorithms.countingSort import countingSort

def radixSort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = countingSort(arr, exp)
        exp *= 10
        
    return arr
        
