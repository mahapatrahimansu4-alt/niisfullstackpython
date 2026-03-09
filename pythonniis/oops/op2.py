class simple:
	def __init__(self,p,t,r):
		self.p=p 
		self.time=t 
		self.rate=r 
	def show(self):
		print("priciple=",self.p)
		print("time=",self.time)
		print("rate=",self.rate)
	def sical(self):
		return self.p*self.time*self.rate/100
i1=simple(1000,10,2)
i1.show()
print("simple intrest=",i1.sical())



