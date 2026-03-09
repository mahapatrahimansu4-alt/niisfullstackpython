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
print("enter princple time and rate")
pr=float(input())
t=float(input())
r=float(input())
i1=simple(pr,t,r)
i1.show()
print("simple intrest=",i1.sical())

