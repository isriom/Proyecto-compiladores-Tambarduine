def LoadCode(fileName):
	path = fileName + ".txt"  # path
	file = open(path)  # abrir
	content = file.readlines()  # lectura de las lineas
	file.close()  # cerrar
	print(content)
	return content


def SaveCode(fileName, dato):
	path = fileName + ".txt"
	with open(path, 'r+') as f:
		f.truncate(0)
	file = open(path, "a")  # a->append
	file.write(dato + "\n")  # escribe el dato en el file
	file.close()


SaveCode("z", "SET @var1, True\nIf\n     @var1.Neg")
saved = LoadCode("z")
print(saved)

# SaveCode("z","")
# SaveCode("z","")
