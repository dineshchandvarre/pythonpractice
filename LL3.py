class Node():
	def __init__(self,value):
		self.value=value #assigning value to node object as self.value
		self.next=None   #assigning None to nodeobject.next 



class Linked_list():              # defining class Linked_list
	def __init__(self,node):				#passing node object as a argument to Linkedlist constructor
		self.head=node 								#assigning node object to linked list pobject as head attribute
		self.end=node
	def insert(self,node):					#defining insert method 
		self.end.next=node 						#
		self.end=node
		# s=self.head
		# while(s.next!=None):
		# 	s=s.next
		# s.next=node
		
	def prin(self):
		h=self.head
		while(h!=None):
			print(h.value)
			h=h.next
	def traver(self,func):
		s=self.head
		li=[]
		while(s!=None):
			li.append(s.value)
			s=s.next
		k=list(map(func,li))
		return k







node=Node(2)
node1=Node(3)
node2=Node(4)
node3=Node(5)
linklist=Linked_list(node)
linklist.insert(node1)
linklist.insert(node2)
linklist.insert(node3)
linklist.prin()
linklist.prin()
print(linklist.traver(lambda x:x*x))


