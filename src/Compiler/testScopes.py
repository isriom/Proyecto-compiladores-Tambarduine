class Var:

	def __init__(self, name, scope):
		self.name = name
		self.scope = scope

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setScope(self, scope):
		self.scope = scope

	def getScope(self):
		return self.scope


def globals(data):
	"""
	function to detect global variables before execute the lexical analise
	:param data: the input code as a string
	:return: list with global variables names
	"""
	globalVars = []
	# print(data2[0:0+2])
	# print ('iiiii')
	newGlobal = False
	varName = ""
	scopeNum = -1
	totalScopes = -1
	# Entradas Salidas
	if 'Principal' in data:
		print('Principal' in data)
		MainPos = data.find('Principal')
		for i in range(MainPos, len(data) - 1):
			# print (data2[i:i+3])
			if data[i:i + 3] == "Set" and scopeNum == 0:
				for j in range(i + 3, len(data) - 1):  # acordarme del brake
					if data[j] == "@":
						varName += "@"
						for k in range(j + 1, len(data) - 1):
							if data[k] == " " or data[k] == "," or data[k] == '.':
								if varName in globalVars:
									varName = ""
									newGlobal = True
									break
								globalVars.append(varName)
								print(globalVars)
								varName = ""
								newGlobal = True
								break
							else:
								varName += data[k]
								print('VARNAME = ' + varName)
					elif newGlobal == True:
						newGlobal = False
						break
			# else:
			# Error no asigna la variable correctamente
			# break

			if data[i] == '{':
				totalScopes += 1
				scopeNum += 1

				print(totalScopes)  ####

			if data[i] == '}':
				totalScopes = scopeNum
				scopeNum -= 1

				print(scopeNum)  ####

	print('END')
	print(globalVars)
	return globalVars
