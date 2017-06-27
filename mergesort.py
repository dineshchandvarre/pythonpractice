# def merge(left, right):
# 	result = []
# 	i,j= 0,0
# 	while i < len (left) and j < len (right): 
# 		if left[i] <= right [j]:
# 			result.append(left[i])
# 			i+=1	
# 		else:
# 			result.append(right[j])
# 			j+=1

# #The loop may break before all elements are copied hence append the remaining elements
# 	result += left[i:]
# 	result += right[j:]
# 	return result

# #The mergesort method to split the arrays into smaller subarrays
# def mergesort(lst):
# 	if len(lst) <= 1:
# 		return lst
# 	middle = int(len(lst) / 2)
# 	left = mergesort(lst[:middle])
# 	right = mergesort(lst[middle:])
# 	return merge(left, right)

# if __name__ == '__main__':
# 	print (mergesort([4,3,1,2,7,90,5,3,2,56,34,122,21]))
def getinput():
    print ("0: start")
    print ("1: stop")
    print ("2: reset")
    x = raw_input("selection: ")
    try:
        num = int(x)
        if num > 2 or num < 0:
            return None
        return num
    except:
        return None
num = getinput()
if not num:
    print ("invalid")
else:
    print ("valid")