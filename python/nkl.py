class calculater1():

	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.add()
		self.sub()
		self.mul()
		self.div()
	def add(self):
		print(f"addition=={self.a+self.b}")
	def sub(self):
		print(f"subraction=={self.a-self.b}")
	def mul(self):
		print(f"mul=={self.a*self.b}")
	def div(self):
		print(f"div=={self.a/self.b}")
obj=calculater1(2,10)
