# waopp to add students and their rno in class

class student:
	def __init__(self, rno, name):
		self.rno = rno
		self.name = name
	def show(self):
		print("rno = ", self.rno)
		print("name = ",self.name)
data = []
while True:
	op = int(input(" 1 add, 2 view and 3 exit"))
	if op == 1:
		rno = int(input("enter rno "))
		name = input("enter name ")
		s = student(rno, name)
		data.append(s)
	elif op == 2:
		for d in data:
			d.show()
	elif op == 3:
		break
	else:
		print("invalid option ")