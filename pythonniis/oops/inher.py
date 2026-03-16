class parent:
	def display_parent(self):
		print("this is parent class")
class child(parent):
	def display_child(self):
		print("this is child calss")
class engineering(child):
	def display_engineering(self):
		print("this is engineering class")
ob=engineering()
ob.display_parent()
ob.display_child()
ob.display_engineering()
