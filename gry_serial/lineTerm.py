import threading
from serial import Serial

class lineTerm(Serial):
	def __init__(self, portname, _baudrate = 9600, _timeout = 0.2):
		super().__init__(portname, baudrate = _baudrate, timeout = _timeout)
		thread = threading.Thread(target=self.read_from_port)
		thread.start()
		self.inputter()


	def handle_data(self): #data
		print(self.data)

	def read_from_port(self):
		self.data = self.readlines()
		self.handle_data()

	def inputter(self):
		while 1:
			ret = input("$: ")
			print("---{}---".format(ret))



