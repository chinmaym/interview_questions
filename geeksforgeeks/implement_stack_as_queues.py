
class Stack():
	def __init__(self):
		self.q1 = []
		self.q2 = []
	def push(self,val):
		self.q2.append(val)
		while len(self.q1) > 0:
			self.q2.append(self.q1[0])
			self.q1 = self.q1[1:]
		self.q1 = self.q2
		self.q2 = []
	def pop(self):
		element = self.q1[0]
		self.q1 = self.q1[1:]
		return  element
	def __str__(self):
		a = map(str,self.q1)
		return  " ".join(a)

def main():
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	print s
	print s.pop()
	print s

if __name__ == '__main__':
	main()