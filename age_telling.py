class persion():
	def __init__(self,a,b,c,d):
		self.day=a
		self.month=b
		self.year=c
		self.name=d
	def name(self):
		print("the value of name is ",self.name)
	def age(self):
		if self.month in [1,3, 5, 7, 8, 10, 12]:
		        print("day",31-self.day)
		elif self.month==2:
			if self.year%4==0 and self.year%100==0:
				print("day",29-self.day)
			else:
				print("day",28-self.day)
		else:
			print("day",30-self.day)
		print("month",12-self.month)

		print("year",2024-self.year)
     

st=persion(28,7,2004,'naresh')
st.age()





