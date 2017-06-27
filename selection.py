def selection_sort(arr):
	for i in range(len(arr)):
		new=arr.index(min(arr[i:len(arr)]))
		swap(arr,new,i)
	print(arr)
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
selection_sort([i for i in range(100)])