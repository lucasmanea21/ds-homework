from algorithms.shellSort import shellSort
from algorithms.timSort import timSort

def bucketSort(arr):
    bucket=[]
    max_value = max(arr)
    for i in range(len(arr)):
        bucket.append([])
    
    for i in range(len(arr)):
        index=int(len(arr)*arr[i]/(max_value+1))
        bucket[index].append(arr[i])
    
    for i in range(len(arr)):
        bucket[i].sort() # implementat cu functia sort din Python
    
    sortedArr=[]
    for i in range(len(arr)):
        sortedArr.extend(bucket[i])
    
    return sortedArr