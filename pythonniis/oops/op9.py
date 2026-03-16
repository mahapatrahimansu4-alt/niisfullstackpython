#setter and getter
class student:
	def __init__(self,n,r,m):
		self.__name=n 
		self.__roll=r 
		self.__mark=m 
	def show(self):
		print("my name",self.__name)
		print("my roll",self.__roll)
		print("my mark",self.__mark)
	def update(self,n,r,m):
		self.__name=n 
		self.__roll=r 
		self.__mark=m 
	def set__Name(self,name):
		self.__name=name 
	def set__Roll(self,roll):
		self.__roll=roll 
	def set__Mark(self,mark):
		self.__mark=mark
	def get__name(self):
		return self.__name
	def get__roll(self):
		return self.__roll  
	def get__mark(self):
		return self.__mark  
s=student("muna",1,90.50)
s.show()
