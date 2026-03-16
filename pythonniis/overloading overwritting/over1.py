class demo:
	def show(self,a):
		print("one argument show",a)
	def show(self,a,b):
		print("two argument show",a,b)
	def show(self):
		print("no argument show")
d=demo()
d.show()