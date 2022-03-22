data = '''>= <= = ==> ,{ SET println! If "textoprueba. @Aqqaae @var26_? type() < .Neg Abanico() ; //% ** 10 -20 AB *2\n True False Fin-EnCaso'''
data2 = ' {}   { {} {} } Principal {  SET @abc SET @var2 SET @var3; SET @var4 , @abs+@var5{ {}  { } } }'

print(data2.find('Principal'))
num = 0;


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


globalVars = []


def Scopes():
	global globalVars
	# print(data2[0:0+2])
	# print ('iiiii')
	newGlobal = False
	varName = ""
	scopeNum = -1
	totalScopes = -1
	# Entradas Salidas
	if 'Principal' in data2:
		print('Principal' in data2)
		MainPos = data2.find('Principal')
		for i in range(MainPos, len(data2) - 1):
			# print (data2[i:i+3])
			if data2[i:i + 3] == "SET" and scopeNum == 0:
				for j in range(i + 3, len(data2) - 1):  # acordarme del brake
					if data2[j] == "@":
						varName += "@"
						for k in range(j + 1, len(data2) - 1):
							if data2[k] == " " or data2[k] == ",":
								globalVars.append(varName)
								print(globalVars)
								varName = ""
								newGlobal = True
								break
							else:
								varName += data2[k]
								print('VARNAME = ' + varName)
					elif newGlobal == True:
						newGlobal = False
						break
			# else:
			# Error no asigna la variable correctamente
			# break

			if data2[i] == '{':
				totalScopes += 1
				scopeNum += 1

				print(totalScopes)  ####

			if data2[i] == '}':
				totalScopes = scopeNum
				scopeNum -= 1

				print(scopeNum)  ####

	print('END')
	print(globalVars)


Scopes()

for i in data2:
	if i == 'Principal':
		print('funciona')
		num += 1;
		print(num)
