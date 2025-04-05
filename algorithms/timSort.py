def insertionSort(arr,st,dr):
	for i in range(st+1,dr+1):
		x=arr[i]
		j=i-1
		while j>=st and arr[j]>x:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=x
	return arr

def merge(arr,st,mij,dr):
	p1=mij-st+1
	p2=dr-mij
	arrSt=[0]*p1
	arrDr=[0]*p2
	i=0
	j=0
	k=st
	while i<p1:
		arrSt[i]=arr[st+i]
		i+=1
	while j<p2:
		arrDr[j]=arr[mij+1+j]
		j+=1
	i=0
	j=0
	while i<p1 and j<p2:
		if arrSt[i]<=arrDr[j]:
			arr[k]=arrSt[i]
			i+=1
		else:
			arr[k]=arrDr[j]
			j+=1
		k+=1
	while i<p1:
		arr[k]=arrSt[i]
		k+=1
		i+=1
	while j<p2:
		arr[k]=arrDr[j]
		k+=1
		j+=1
		
def timSort(arr):
	n=len(arr)
	r=32
	i=0
	st=0
	size=r
	while i<n:
		tmp=min(i+r-1,n-1)
		insertionSort(arr,i,tmp)
		i+=r
	while size<n:
		st=0
		while st<n:
			mij=st+size-1
			dr=min(st+2*size-1,n-1)
			if mij<dr:
				merge(arr,st,mij,dr)
			st+=2*size
		size*=2
	return arr

