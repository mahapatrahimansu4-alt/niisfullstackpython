class P:
	def property(self):
		print("land+money+car")
	def marry(self):
		print("sita")
class C(P):
	def marry(self):
		print("gita")
ob=C()
ob.property()
ob.marry()