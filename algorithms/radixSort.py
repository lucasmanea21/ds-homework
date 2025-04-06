from algorithms.countingSort import countingSort

def radixSort(arr):
    if not arr:
        return arr
    
    arr = list(map(int, arr))
    max_val = max(arr)
    exp = 1
    shift = 0
    mask = (1 << 16) - 1  # 65535

    while (max_val >> shift) > 0:
        arr = countingSort(arr, shift, mask)
        shift += 16

    return arr
        
