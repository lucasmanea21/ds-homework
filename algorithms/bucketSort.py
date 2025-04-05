def bucketSort(arr):
    bucket=[]

    for i in range(len(arr)):
        bucket.append([])
    
    for j in arr:
        index=int(10*j)
        bucket[index].append(j)
    
    for i in range(len(arr)):
        bucket[i].sort() # implementat cu functia sort din Python
    
    sortedArr=[]
    for i in range(len(arr)):
        sortedArr.extend(bucket[i])
    
    return sortedArr
    