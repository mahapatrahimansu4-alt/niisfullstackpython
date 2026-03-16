#passing object reference in argument.
class student:
	def __init__(self,n,r,m):
		self.name=n 
		self.roll=r 
		self.mark=m  
	def show(self):
		print("my name=",self.name)
		print("my roll=",self.roll)
		print("my mark=",self.mark)
s=student("himansu",25,88)
s.show()