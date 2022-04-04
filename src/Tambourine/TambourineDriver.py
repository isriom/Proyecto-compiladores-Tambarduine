import serial
import time


class TambourineDriver:
	"""
	class to comunicate with the Hardware using serial comunication
	"""

	def __init__(self):
		self.metronomeTime = 0.3
		self.tambourine = serial.Serial(port='COM4', baudrate=115200, timeout=.3)
		self.tambourine.isOpen()

		print("Opened port")


	def writeMsg(self, x):
		"""
		Send a Mesaage with the action to the Hardware, order are sended as a encoded string and the hardware decode an execute
		:param x:
		:return:
		"""
		try:
			self.tambourine.write(bytes(x, 'utf-8'))
			time.sleep(0.05)
			self.tambourine.flush()
		except:
			self.tambourine.close()
			time.sleep(0.05)
			self.tambourine.open()
			self.tambourine.flush()
		time.sleep(self.metronomeTime)

	def abanico(self, Dir):
		"""
		Abanico order encode
		:param Dir:
		:return:
		"""
		if Dir == 'A':
			self.writeMsg('1A')
		elif Dir == 'B':
			self.writeMsg('1B')
		print("Abanico")

	def vertical(self, Dir):
		"""
		Vertical order encode
		:param Dir:
		:return:
		"""
		if Dir == 'D':
			self.writeMsg('2D')
		elif Dir == 'I':
			self.writeMsg('2I')
		print("Vertical")

	def percutor(self, Side):
		"""
		percutor order encode
		:param Side:
		:return:
		"""
		if Side == 'D':
			self.writeMsg('3D')
		if Side == 'I':
			self.writeMsg('3I')
		if Side == 'A':
			self.writeMsg('3A')
		if Side == 'B':
			self.writeMsg('3B')
		if Side == 'DI':
			self.writeMsg('3DI')
		if Side == 'AB':
			self.writeMsg('3AB')
		print("Percutor")

	def golpe(self):
		"""
		golpe order encode
		:return:
		"""
		self.writeMsg('4')
		print("Golpe")

	def vibrato(self, Quantity):
		"""
		vibrato order encode
		:param Quantity:
		:return:
		"""
		self.writeMsg('V' + str(Quantity))
		time.sleep(0.2 * Quantity)
		print("Vibrato")

	def metronomo(self, State, Range):
		self.metronomeTime = Range
		"""
		metronome order encode
		:param State:
		:param Range:
		:return:
		"""
		if Range >= 0.5:
			if State == 'A':
				self.writeMsg('MA' + str(Range))
				print("Metronomo Activado")
			elif State == 'D':
				self.writeMsg('MD')
				print("Metronomo Desactivado")

def main():
	tambor = TambourineDriver()
	tambor.vibrato(6)
main()