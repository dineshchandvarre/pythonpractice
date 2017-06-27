def search(li,num):
	for i in li:
		if(i==num):
			return True
	return False

print(search([12,13,14,15,16],13))

