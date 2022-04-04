from libs.ply.lex import LexToken
from libs.ply.yacc import YaccSymbol
from src.ProjectParser.Parser import *
from src.Compiler.testScopes import *


# from src.Tambourine.TambourineDriver import *


class Scope:
	"""
	Class that represent a Scope, works a symbol table to that scope
	"""

	def __init__(self, t, comp):

		self.variables = {}
		self.lineno = t.lineno
		self.lexpos = t.lexpos
		self.previous = None
		self.toCheck = []
		self.toCheckFor = []
		self.toCheckConditions = []
		self.toCheckAD = []
		self.toCheckR = []
		self.code = ''
		self.comp = comp
		self.gl = []
		pass

	def SetLineno(self, t):
		"""
		Deprecated
		:param t:
		:return:
		"""
		self.lineno = t.lineno
		self.lexpos = t.lexpos

	def GetType(self, t):
		"""
		Check if a variable already exist in the scope and return it type
		:param t: variable name
		:return: None id no exist, type if declared
		"""
		if not (t in self.variables):
			return None
		else:
			return self.variables[t]

	def insert(self, t):
		"""
		insert a new variable in the scope when declared. Deference between Param, and redeclarations.
		:param t: tuple from gramatic rules that contain the information of the variable
		:return:
		"""
		if t[0][0] == 'def':
			t[0][1].value += t[1]
		if t[0] == 'PARAM':
			self.insertP(t[1])
			return
		elif t[1] == 'bool' and (not t[0][1].value in self.variables):
			t = (t[0], 'BOOL')

		if type(t[1]) == str and (not t[0][1].value in self.variables):
			self.variables[t[0][1].value] = t[1]
		else:
			try:
				tmpvalue = self.GetType(t[1].value[1].value)
			except:
				tmpvalue = self.GetType(t[0][1].value)
			if tmpvalue == None:
				self.insertCheck(('ADJUST', t[0], t[1]))
			elif tmpvalue != self.GetType(t[0][1].value):
				self.insertCheck(('ADJUST', t[0], t[1]))
			elif tmpvalue != t[1]:
				self.comp.errors += "La variable " + str(
					t[0][1].value) + " es de tipo " + tmpvalue + " pero se le desea asignar un " + t[
					                    1] + " en linea " + str(t[0][1].lineno) + " indice: " + str(t[0][1].lexpos)
			else:
				self.variables[t[0]] = tmpvalue

	def insertP(self, t):
		"""
		aux function to unpackage Parameters
		:param t: tuple that contains all the parameters data
		:return:
		"""
		if t[0] == 'var' and (not t[1].value in self.variables):
			self.insert(((t[0], t[1]), 'PARAM'))
		elif t[0] == 'ParameterIncomplete':
			for i in t:
				if type(i) == YaccSymbol:
					self.insertP(i.value)

		if t[1].type == 'ParameterIncomplete':
			for i in t[1].value:
				if type(i) == YaccSymbol:
					self.insertP(i.value)
			return
		else:
			return

	def insertCheck(self, checkTuple):
		"""
		insert a check in their respective level
		:param checkTuple: tuple that contain all the data to do check
		:return:
		"""
		if checkTuple[0] == 'CON' or checkTuple[0] == 'NUMBER':
			self.toCheckConditions.append(checkTuple)
		elif checkTuple[0] == 'FOR':
			self.toCheckFor.append(checkTuple)
		elif checkTuple[0] == 'ADJUST':
			self.toCheckAD.append(checkTuple)
		elif checkTuple[0] == 'Exec':
			self.toCheckR.append(checkTuple)
		else:
			self.toCheck.append(checkTuple)

	def RemoveCheck(self):
		"""
		Remove last standar check
		:return:
		"""
		self.toCheck.pop()

	def AddScope(self, scope):
		"""
		link actual scope with a new scope to use inf For check
		:param scope: old scope
		:return:
		"""
		self.previous = scope
		pass

	def Check(self):
		"""
		Semantic analisis implementation, execute all the checks stacked in the AST creation
		work with level
		first -> variables value changes
		second -> standar checks (Types, Neg, T, F)
		third -> conditional checks (int condition int)
		fourth -> For checks, let define if a For variable exist or not
		fifth -> Check Rutines existence and check paramater number coincidence
		:return: Error founded in the semantic analisis
		"""
		error = ''
		print(self.variables)
		for i in self.toCheckAD:
			if i[0] == 'ADJUST':
				vartype = None
				a = i[1][1].value
				b = i[2].value[1].value
				if self.GetType(a) == None:
					if self.GetType(b) == None:
						vartype = self.comp.Scopes['globalScope'].GetType(b)
						self.variables[a] = vartype
					else:
						self.variables[a] = self.GetType(b)
					self.toCheckAD.remove(i)
				else:
					if self.GetType(a) == 'PARAM' or self.GetType(b) == 'PARAM':
						continue
					if self.GetType(a) == self.GetType(b):
						self.toCheckAD.remove(i)
					else:
						error += 'la Variable ' + a + ' y la variable ' + b + ' son diferentes tipos y no pueden ser asignados, Linea ' + \
						         i[2].lineno
		for i in self.toCheck:
			if i[0] == 'TYPEOF':
				vartype = self.GetType(i[1])
				if vartype == None:
					vartype = self.comp.Scopes['globalScope'].GetType(i[1])
					if vartype != None:
						i[2].globalvar = True
						self.gl.append(i[1])
				i[2].defined = vartype
				self.variables[i[1]] = vartype
				if i[2].defined == None:
					for For in self.toCheckFor:
						if i[1] == For[1].value[1].value:
							i[2].defined = 'FOR'
				if i[2].defined == None:
					error += 'La variable ' + i[1] + ' No se encuentra definida. Linea:' + str(
						i[2].value[1].lineno) + ' Indice: ' + str(i[2].value[1].lexpos) + '\n'
				self.toCheck.remove(i)

			elif i[0] == 'NEG':
				vartype = self.GetType(i[1][1].value)
				if vartype == None:
					vartype = self.comp.Scopes['globalScope'].GetType(i[1][1].value)
				if (vartype == 'BOOL'):
					self.toCheck.remove(i)
				else:
					error += 'Var: ' + i[1][1].value + ' is not a bolean. Line: ' + str(i[1][1].lineno)
					self.toCheck.remove(i)

			elif i[0] == 'T':
				vartype = self.GetType(i[1][1].value)
				if vartype == None:
					vartype = self.comp.Scopes['globalScope'].GetType(i[1][1].value)
				if (vartype == 'BOOL'):
					self.toCheck.remove(i)
				else:
					error += 'Var: ' + i[1][1].value + ' is not a bolean. Line: ' + str(i[1][1].lineno)
					self.toCheck.remove(i)

			elif i[0] == 'F':
				vartype = self.GetType(i[1][1].value)
				if vartype == None:
					vartype = self.comp.Scopes['globalScope'].GetType(i[1][1].value)
				if (vartype == 'BOOL'):
					self.toCheck.remove(i)
				else:
					error += 'Var: ' + i[1][1].value + ' is not a bolean. Line: ' + str(i[1][1].lineno)
					self.toCheck.remove(i)
		for i in self.toCheckConditions:
			if i[0] == 'CON':
				a = i[1].value[1]
				a1 = i[1].value[1]
				b = i[2].value[1]
				b1 = i[2].value[1]

				if a.type == 'expression' or b.type == 'expression':
					self.toCheckConditions.remove(i)
					continue
				if type(a) == YaccSymbol:

					a1 = a.value[1].value
					a = a.defined
				else:
					a1 = a.type
					a = a.type
				if type(b) == YaccSymbol:
					b1 = b.value[1].value
					b = b.defined
				else:
					b1 = b.value
					b = b.type
				if a != b:
					if a == 'PARAM' or b == 'PARAM':
						self.toCheckConditions.remove(i)
						continue
					print(i)
					condition = i[3].value[1]
					error += 'Error in the condition: ' + str(a1)
					error += condition.value + str(b1) + ' diferent types conditional' + ' in Line: ' + str(
						condition.lineno)
				print(i)
				self.toCheckConditions.remove(i)
		for i in self.toCheckFor:
			vartype = self.GetType(i[1].value[1].value)
			if vartype == None:
				vartype = self.comp.Scopes['globalScope'].GetType(i[1].value[1].value)
				if vartype == None:
					i[1].defined = i[0]
					self.variables[i[1].value[1].value] = i[0]
			self.toCheckFor.remove(i)

			pass
		for i in self.toCheckR:
			rcuantity = self.comp.Scopes['Rutinas'].GetType(i[1]+str(i[2].number))
			if rcuantity == None:
				error += 'Erorr en linea ' + str(i[2].value[2].lineno) + '. Rutina ' + i[
					1] + ' no se encuentra declarada.'
			if rcuantity == str(i[2].number):
				self.toCheckR.remove(i)
			else:
				error += 'Erorr en linea ' + str(i[2].value[2].lineno) + '. Rutina ' + i[1] + ' recibe ' + str(
					rcuantity) + ' parametros, pero ' + str(i[2].number) + ' fueron entregados\n'

			pass
		return error


class Compiler:
	"""
	Class that do the lexical analize, the sintax analize and transalate the input code to the objective code
	"""

	def __init__(self):
		abstracT = LexToken
		abstracT.lineno = 0
		abstracT.lexpos = 0
		# initial actualScope is the scope in charge of the Rutines. Redefined as a abstract Scope with not linno
		self.Scopes = {'actualScope': Scope(abstracT, self), 'globalScope': None, 'all': []}
		self.lexer = GetLexer()
		self.parser = GetParser()
		self.parser.Comp = self
		self.tablevel = 0
		self.code = ''
		self.status: tuple = ("Init complete",)
		self.errors: str = ''

	def Parse(self, text):
		"""
		Main function to parse a code, call the lexical, sintax, semantic, translation functions
		:param text: code as a single line code
		:return: AST used in the transalation procces
		"""
		# glabal variables finded before start the parse to simplificate posterior work
		gl = globals(text)
		# abstraction of a lextoken to create the intial actual scope
		abstracT = LexToken
		abstracT.lineno = 0
		abstracT.lexpos = 0
		DEFSCOPE = Scope(abstracT, self)
		self.lexer.error = ''
		self.parser.error = ''
		self.Scopes = {'actualScope': DEFSCOPE, 'globalScope': None, 'all': [], 'Rutinas': DEFSCOPE}
		self.status = ("inited",)
		self.errors = ''
		self.code = 'from src.Tambourine.TambourineDriver import *\n'
		# parse the code, call both lexical and sintax analisis
		parse = self.parser.parse(text, debug=True, lexer=self.lexer)
		self.errors += self.lexer.error
		print("self.errors")
		print(self.errors)
		self.errors += self.parser.error
		print(self.errors)
		# if error found in the lexical or sintax stop and save error logs
		if self.errors != '':
			self.status = ("Compilacion finalizada\n", 'Errores: ' + self.errors)
			return parse
		# especial case for global variables scope
		if self.Scopes['globalScope'] == None:
			self.errors += "Error detectando la funcion Principal"
			self.status = ("Compilacion finalizada\n", 'Errores: ' + self.errors)
			return
		self.errors += self.Scopes['globalScope'].Check()
		# init the semantic analise
		for scope in self.Scopes['all']:
			self.errors += scope.Check()
		# insert the globals detected before in the global scope and in the code
		self.Scopes['globalScope'].gl = gl
		for i in gl:
			self.code += 'global ' + i[1:] + '\n'
		# translated the code to the objective Code
		self.code += self.readTree(parse)
		self.errors += self.lexer.error
		if self.errors == '':
			self.errors += 'No se han encontrado errores en el codigo'
		# save actual state with error log
		self.status = ("Compilacion finalizada\n", 'Errores: ' + self.errors)
		print(self.status)
		# add execution order to objective code
		self.code += 'def main(IDE):\n' \
		             '\tglobal Tambourdine\n' \
		             '\tglobal TambourdineIDE\n' \
		             '\tTambourdineIDE=IDE\n' \
		             '\tTambourdine=TambourineDriver()\n' \
		             '\tPrincipal()\n' \
		             'main(IDE)'
		return parse

	def GetCode(self):
		return GetCode()

	def Gettype(self, t):
		if self.Scopes['actualScope'] is not None:
			return self.Scopes['actualScope'].GetType(t)
		else:
			return None

	def Insert(self, T):
		self.Scopes['actualScope'].insert(T)

	def insertCheck(self, checkTuple):
		self.Scopes['actualScope'].insertCheck(checkTuple)

	def RemoveCheck(self):
		self.Scopes['actualScope'].RemoveCheck()

	def AddGlobal(self, Scope):
		if self.Scopes['globalScope'] != None:
			raise SyntaxError
		else:
			self.Scopes['globalScope'] = Scope
		pass

	def CreateScope(self, T):
		"""
		Create and insert a new scope to work as a symbol table
		:param T: Token of pre_scope symbol to define postion of scope
		:return: the new Scope
		"""
		new = Scope(T, self)
		new.AddScope(self.Scopes['actualScope'])
		self.Scopes['all'].append(new)
		self.Scopes['actualScope'] = new
		return new

	def CloseScope(self):
		"""
		Close the actual scope to protect local variables
		:return:
		"""
		if self.Scopes['actualScope'].previous != None:
			self.Scopes['actualScope'] = self.Scopes['actualScope'].previous

	def readTree(self, ast, tablevel=0):
		"""
		Recursive tail function that read the AST and translate it to objective code
		:param ast: AST create with the function Parse, or a node of the AST
		:param tablevel: actual python tab level
		:return: Objective Code
		"""
		if ast is None:
			return
		if type(ast) == YaccSymbol:
			ast = ast.value
		if type(ast) == LexToken:
			ast = (ast.type, ast.value, ast)
		length = len(ast)

		Code = ''
		if ast[0] == 'ENDLINE':
			return ''
		if ast[0] == ':':
			return ''
		elif ast[0] == 'instruction':
			for instruction in range(1, length):
				Code += self.readTree(ast[instruction], tablevel)

		elif ast[0] == 'ifelsestatement':
			Code += self.readTree(ast[1], tablevel) + '\n'
			Code += self.readTree(ast[2], tablevel)

		elif ast[0] == 'elsestatement':
			Code += ("\t" * tablevel) + "else" + ":\n"
			Code += self.readTree(ast[2], tablevel + 1)

		elif ast[0] == 'ifstatement':
			Code += ("\t" * tablevel) + "if " + self.readTree(ast[2]) + ":\n"
			Code += self.readTree(ast[3], tablevel + 1)

		elif ast[0] == 'forstatement':  # need a refactor
			if len(ast) >= 7:
				vartype = ast[7].scope.previous.GetType(ast[2].value[1].value)
			else:
				vartype = ast[5].scope.previous.GetType(ast[2].value[1].value)

			if vartype == 'FOR' or vartype == None:
				Code += ("\t" * tablevel) + "for " + self.readTree(ast[2]) + 'in range( 1,' + self.readTree(ast[4])
			else:
				Code += ("\t" * tablevel) + "for " + self.readTree(ast[2]) + ' in range(' + self.readTree(
					ast[2]) + ',' + self.readTree(ast[4])
			if length > 6:
				Code += ',' + self.readTree(ast[6])
				Code += '):\n' + self.readTree(ast[7], tablevel + 1)
			else:

				Code += '):\n' + self.readTree(ast[5], tablevel + 1)

		elif ast[0] == 'incasestatement':  # call a aux function to save variable name of case statements
			if length == 5:
				Code += ("\t" * tablevel) + self.readTree(ast[2])
				Code += ("\t" * tablevel) + self.readTree(ast[3])
			else:
				Code += self.ENCASO(ast[3], tablevel, self.readTree(ast[2]))

		elif ast[0] == 'defstatement':
			Code += ("\t" * tablevel) + 'def '
			if length == 5:
				Code += self.readTree(ast[2]) + self.readTree(ast[3]) + ':\n'
				Code += ("\t" * tablevel) + self.readTree(ast[4], tablevel + 1) + '\n'
			else:
				Code += 'Principal()' + ':\n'
				Code += ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1) + '\n'

		elif ast[0] == 'excecstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + self.readTree(ast[3]) + "\n"

		elif ast[0] == 'printstatement':
			Code += ("\t" * tablevel) + 'TambourdineIDE.print' + self.readTree(ast[2]) + "\n"

		elif ast[0] == 'metronomostatement':
			Code += ("\t" * tablevel) + 'Tambourdine.metronomo(' + self.readTree(ast[3]) + ',' + self.readTree(
				ast[5]) + ")\n"

		elif ast[0] == 'declarationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=' + self.readTree(ast[4]) + "\n"

		elif ast[0] == 'negationstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=not ' + self.readTree(ast[2]) + "\n"

		elif ast[0] == 'tfstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=True ' + "\n"

		elif ast[0] == 'ffstatement':
			Code += ("\t" * tablevel) + self.readTree(ast[2]) + '=False ' + "\n"

		elif ast[0] == 'abanicostatement':
			Code += ("\t" * tablevel) + 'Tambourdine.abanico(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'verticalstatement':
			Code += ("\t" * tablevel) + 'Tambourdine.vertical(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'percutorstatement':
			Code += ("\t" * tablevel) + 'Tambourdine.percutor(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'golpestatement':
			Code += ("\t" * tablevel) + "Tambourdine.golpe()\n"

		elif ast[0] == 'vribatoestatement':
			Code += ("\t" * tablevel) + 'Tambourdine.vibrato(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'typeestatement':

			Code += ("\t" * tablevel) + 'type(' + self.readTree(ast[3]) + ")\n"

		elif ast[0] == 'expressionestatement':
			Code += ("\t" * tablevel) + self.readTree(ast[1])

		elif ast[0] == 'Scope':
			for gl in ast[2].scope.gl:
				Code += ("\t" * tablevel) + 'global ' + gl[1:] + '\n'
			Code += self.readTree(ast[3], tablevel)

		elif ast[0] == 'whenestatement':
			if length <= 3:
				Code += ("\t" * tablevel) + self.readTree(ast[1])
				Code += ("\t" * tablevel) + self.readTree(ast[2])
			else:
				Code += ("\t" * tablevel) + "if" + self.readTree(ast[2]) + self.readTree(ast[3]) + self.readTree(
					ast[4]) + ":\n"
				Code += ("\t" * tablevel) + self.readTree(ast[6], tablevel + 1)

		elif ast[0] == 'whenelseestatement':
			Code += ("\t" * tablevel) + "Else" + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[2], tablevel + 1)

		elif ast[0] == 'Parameters':
			Code += self.readTree(ast[1]) + self.readTree(ast[2])

		elif ast[0] == 'ParameterIncomplete':
			if length == 3:
				Code += self.readTree(ast[1]) + self.readTree(ast[2])
			else:
				Code += self.readTree(ast[1]) + ',' + self.readTree(ast[3])

		elif ast[0] == 'text':
			Code += self.readTree(ast[1]) + self.readTree(ast[2])

		elif ast[0] == 'textincomplete':
			Code += self.readTree(ast[1]) + ' ' + self.readTree(ast[2])

		elif ast[0] == 'var':
			Code += self.readTree(ast[1])

		elif ast[0] == 'numberParam':
			if length == 3:
				Code += self.readTree(ast[1]) + self.readTree(ast[2])
			elif length == 4:
				Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])
			else:
				Code += self.readTree(ast[1])

		elif ast[0] == 'boolParam':
			if length == 4:
				Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])
			else:
				Code += self.readTree(ast[1])

		elif ast[0] == 'condition':
			Code += self.readTree(ast[1])

		elif ast[0] == 'Pre_Scope':
			Code += ''

		elif ast[0] == 'expression':
			Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])

		elif ast[0] == 'bool':
			if length == 4:
				Code += self.readTree(ast[1]) + self.readTree(ast[2]) + self.readTree(ast[3])
			else:
				Code += self.readTree(ast[1])

		elif ast[0] == 'VAR':
			Code += ast[1][1:] + ' '

		elif ast[0] == 'NUMBER':
			Code += str(ast[1])
		elif ast[0] in letters:
			Code += "'" + ast[1] + "'"
		else:
			return ast[1]
		return Code

	def ENCASO(self, ast, tablevel, parametro):
		"""
		Aux function of readTree. Recursive save state function to unpack Encase statements without explicit variable.
		:param ast:
		:param tablevel:
		:param parametro:
		:return:
		"""
		if type(ast) != tuple:
			ast = ast.value
		length = len(ast)
		Code = ''
		if length <= 3:
			Code += ("\t" * tablevel) + self.ENCASO(ast[1], tablevel, parametro)
			Code += ("\t" * tablevel) + self.ENCASO(ast[2], tablevel, parametro)
		else:
			Code += ("\t" * tablevel) + "if" + parametro + self.readTree(ast[2]) + self.readTree(ast[3]) + ":\n"
			Code += ("\t" * tablevel) + self.readTree(ast[5], tablevel + 1) + "\n"
		return Code
		pass


if __name__ == '__main__':
	# Possible correccion del error de working directory
	# import sys, os
	# print(os.getcwd())
	# os.chdir("../../")
	# print(os.getcwd())

	comp = Compiler()
	ast = comp.Parse(

		'''Def @MiRutina2 (@abc){ 
				Set @xy1, 4;
				Set @xy2, 4;
			}
			Def @hitxX (@xhits){
				Set @Var1, @xhits;
				for @Var1 to 10 Step 2{
				Golpe();
				println! ("golpe_numero: ", @Var1 ); 
				}
			}
			
			Def @FiboHit(@max,@actual){
				Set @Run, True;
				If (@actual > @max){
				Set @Run,False;
				println!("FIN");
				}
				Else{
				Exec @FiboHit(@max,@actual+1);
				}
			}
			
			Def Principal (){
				Set @Variable1, 5; # Variables globales
				Set @xy1, 5;
				Metronomo('A',0.4);
				Exec @hitxX(@xy1);
			}''')
	print(comp.errors)
	File = open("Rutina.py", "w")
	File.write(comp.code)
	File.close()
	print('ast:\n')
	print(ast)
