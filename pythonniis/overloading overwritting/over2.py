#overloading support using default 	parameter.
class demo:
	def show(self,a=None,b=None):
		if a!=None and b!=None:
			print("two argument show",a,b)
		elif a!=None:
			print("one argument show",a)
		else:
			print("no argument show")
d=demo()
d.show()
d.show(10)
d.show(10,20)