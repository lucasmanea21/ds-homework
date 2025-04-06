def countingSort(arr, exp):
    if not arr:
        return arr
    
    n = len(arr)
    output = [0] * n
    count = [0]*10
    
    for num in arr:
        index = int((num // exp) % 10)
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in reversed(range(n)):
        index = int((arr[i] // exp) % 10)
        count[index] -= 1
        output[count[index]] = arr[i]

    return output
    