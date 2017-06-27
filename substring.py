import string	
def Subtrings(string,n):
	string=	string.replace(" ","")
	li=[]
	for i in range( len( string ) -n+1):
		li.append(string[ i : i+n ])
	print (li)
Subtrings("hello how are you",3)
