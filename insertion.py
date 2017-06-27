
# 	arr2[]
# 	count=1
# 	comparison_count = 0
# 	for i in range(len(arr1)):
# 		for j in range(len(arr)-count):
# 			if (arr[j-1]<arr[i]>arr[j+1]): 
# 				arr[i]=arr[j]
# 		# count+=1
# 	print (count-1)

# 	print(arr)

# insertion([6,4,2,5,3,1])
def insertion(arr1):
	a=[]
	for i in range(1,len(arr1)):
		for j in range(len(a)+1):
			if(arr1[i]<a[j]):
				a[j]=arr1[i]
				a.append(a[j])
	print(a)
insertion([6,4,2,5,3,1])
