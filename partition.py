import math
def partition(a):
	p=0	
	r=len(a)-1
	i=p-1
	x=a[r]
	print(x)
	for j in range(len(a)):
		if(a[j]<x):
			i+=1
			a[i],a[j]=a[j],a[i]
	a[r],a[i+1]=a[i+1],a[r]
	print(i+1)
	print(a[:i])
	print(a[i:])


def greet(name):
	return "hello "+ name


def partition2(a):
	print(a)
	if(len(a) == 1):
		return 
	i,j = 0, len(a)-1
	pivot_index = math.floor(len(a)/2)
	pivot = a[pivot_index]
	print (pivot)
	while i<j:

		while a[i] < pivot:
			i+=1
		while a[j]>pivot:
			j-=1
		# print(i,j,a[i],a[j])
		if(i<j):	
			a[i],a[j] = a[j], a[i]
			i+=1
			j-=1
	print (a)		
	if(j>0):
		partition2(a[:j])
	if(i<len(a)-1):	
		partition2(a[i:])				
	# return a	
# print(partition2([2,4,5,12,11,3,345,9]))
a = [2,4,5,12,11,3,345,9]
# a = [345,9]
partition2(a)
print(a)

b = greet("sagar")
