import serial
import time


class TambourineDriver:
	def __init__(self):
		try:
			self.tambourine = serial.Serial(port='COM5', baudrate=115200, timeout=.31)
			self.tambourine.isOpen()
			print("Opened port")
		except IOError:
			pass
			self.tambourine.close()
			self.tambourine.open()
			print("Port re-opened")

	def writeMsg(self, x):
		try:
			self.tambourine.write(bytes(x, 'utf-8'))
			time.sleep(0.05)
			self.tambourine.flush()
		except:
			self.tambourine.close()
			time.sleep(0.05)
			self.tambourine.open()
			self.tambourine.flush()

	def abanico(self, Dir):
		if Dir == 'A':
			self.writeMsg('1A')
		elif Dir == 'B':
			self.writeMsg('1B')
		print("Abanico")

	def vertical(self, Dir):
		if Dir == 'D':
			self.writeMsg('2D')
		elif Dir == 'I':
			self.writeMsg('2I')
		print("Vertical")

	def percutor(self, Side):
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
		self.writeMsg('4')
		print("Golpe")

	def vibrato(self, Quantity):
		for i in range(Quantity):
			if i % 2 == 0:
				self.writeMsg('2D')
				time.sleep(0.1)
			else:
				self.writeMsg('2I')
				time.sleep(0.1)
		print("Vibrato")

	def metronomo(self, State, Range):
		if Range >= 0.5:
			if State == 'A':
				self.writeMsg('MA' + str(Range))
				print("Metronomo Activado")
			elif State == 'D':
				self.writeMsg('MD')
				print("Metronomo Desactivado")
