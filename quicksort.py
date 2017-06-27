import string
import sys
def partition(a):
	p=0	
	r=len(a)-1
	i=p-1
	x=a[r]
	for j in range(len(a)):
		if(a[j]<=x):
			i+=1
			a[i],a[j]=a[j],a[i]
	a[r],a[i+1]=a[i+1],a[r]
	return i+1




quicksort([2,4,11,3,5,9,7,6])

