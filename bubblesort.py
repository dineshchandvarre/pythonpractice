def bubble_sort(arr):
	count=1
	comparison_count = 0
	for i in range(len(arr)):
		for j in range(len(arr)-count):
			if (arr[j-1]<arr[i]>arr[j+1]): 
				arr[i]=arr[j]
		# count+=1
	print (count-1)

	print(arr)

bubble_sort([6,4,2,5,3,1])
